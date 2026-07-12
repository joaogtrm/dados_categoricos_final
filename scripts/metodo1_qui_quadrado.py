"""
Método 1: qui-quadrado de independência + V de Cramér + resíduos de Pearson
Rede de Ensino x (Área Geral CINE, Grau Acadêmico, Modalidade de Ensino).

Saídas em: resultados/metodo1/
    residuos_area_geral.csv    — resíduos padronizados de Pearson (Rede x Área Geral)
    residuos_grau.csv          — resíduos padronizados de Pearson (Rede x Grau Acadêmico)
    residuos_modalidade.csv    — resíduos padronizados de Pearson (Rede x Modalidade)
"""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

BASE = Path(__file__).resolve().parent.parent
PKL = BASE / "dados" / "base_categorica_2024.pkl"
OUT = BASE / "resultados" / "metodo1"
OUT.mkdir(parents=True, exist_ok=True)

MAPA_REDE = {1: "Pública", 2: "Privada"}
MAPA_GRAU = {1: "Bacharelado", 2: "Licenciatura", 3: "Tecnológico"}
MAPA_MODALIDADE = {1: "Presencial", 2: "EAD"}

VARS = {
    "area_geral": "Área Geral",
    "grau": "Grau Acadêmico",
    "modalidade": "Modalidade",
}


def cramer_v(tab: pd.DataFrame, chi2: float) -> float:
    n = tab.values.sum()
    k = min(tab.shape) - 1
    return np.sqrt(chi2 / (n * k))


def residuos_padronizados(tab: pd.DataFrame, esperado: np.ndarray) -> pd.DataFrame:
    n = tab.values.sum()
    p_linha = tab.sum(axis=1).to_numpy() / n
    p_coluna = tab.sum(axis=0).to_numpy() / n
    denom = np.sqrt(esperado * np.outer(1 - p_linha, 1 - p_coluna))
    return pd.DataFrame((tab.values - esperado) / denom, index=tab.index, columns=tab.columns)


def testar_associacao(df: pd.DataFrame, var: str, nome: str) -> dict:
    tab = pd.crosstab(df["rede"], df[var])
    tab.index.name, tab.columns.name = "Rede", nome
    chi2, p, gl, esperado = chi2_contingency(tab)
    return {
        "tabela": tab,
        "chi2": chi2,
        "gl": gl,
        "p": p,
        "cramer_v": cramer_v(tab, chi2),
        "residuos": residuos_padronizados(tab, esperado).round(2),
    }


print("Carregando base...")
df = pd.read_pickle(PKL)
df["rede"] = df["TP_REDE"].astype(object).map(MAPA_REDE)
df["grau"] = df["TP_GRAU_ACADEMICO"].astype(object).map(MAPA_GRAU)
df["modalidade"] = df["TP_MODALIDADE_ENSINO"].astype(object).map(MAPA_MODALIDADE)
df["area_geral"] = df["NO_CINE_AREA_GERAL"]

for var, nome in VARS.items():
    r = testar_associacao(df, var, nome)
    p_str = "< 2.2e-16" if r["p"] < 2.2e-16 else f"{r['p']:.4g}"
    print(f"\n==== Rede x {nome} ====")
    print(f"qui-quadrado = {r['chi2']:.1f}, gl = {r['gl']}, p-valor {p_str}, "
          f"V de Cramér = {r['cramer_v']:.3f}")
    print("Resíduos padronizados de Pearson (>|2| = célula puxa a associação):")
    print(r["residuos"])
    r["residuos"].to_csv(OUT / f"residuos_{var}.csv", encoding="utf-8-sig")

print(f"\nConcluído. Saídas em: {OUT}")
