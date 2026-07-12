"""
Análise descritiva exploratória da base categórica do Censo da
Educação Superior 2024. Gera medidas descritivas (univariadas e
bivariadas contra TP_REDE) e gráficos. Tudo é salvo em disco para
uso posterior — nenhuma figura é exibida na tela.

Saídas em: resultados/descritiva/
    resumo_univariado.csv              — visão geral de todas as variáveis
    tabelas/freq_<VAR>.csv             — frequências absolutas e relativas
    tabelas/crosstab_<VAR>_por_rede.csv          — contagem por TP_REDE
    tabelas/crosstab_pct_<VAR>_por_rede.csv      — % dentro de cada rede
    graficos/uni_<VAR>.png             — barras univariadas
    graficos/bi_<VAR>_por_rede.png     — barras agrupadas por TP_REDE
    graficos/heatmap_<VAR>_por_rede.png — heatmap de proporções
"""
#
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import entropy

BASE = Path(__file__).resolve().parent.parent
PKL = BASE / "dados" / "base_categorica_2024.pkl"
OUT = BASE / "resultados" / "descritiva"
TAB = OUT / "tabelas"
GRA = OUT / "graficos"
for d in (TAB, GRA):
    d.mkdir(parents=True, exist_ok=True)

# ---------- nomes amigáveis das variáveis (conforme tabela "Base de Dados" do artigo) ----------
NOMES = {
    "TP_REDE": "Rede de Ensino",
    "TP_CATEGORIA_ADMINISTRATIVA": "Categoria Administrativa",
    "NO_CINE_AREA_GERAL": "Área Geral",
    "NO_CINE_AREA_ESPECIFICA": "Área Específica",
    "NO_CINE_AREA_DETALHADA": "Área Detalhada",
    "TP_NIVEL_ACADEMICO": "Nível Acadêmico",
    "TP_GRAU_ACADEMICO": "Grau Acadêmico",
    "TP_MODALIDADE_ENSINO": "Modalidade de Ensino",
    "TP_ORGANIZACAO_ACADEMICA": "Organização Acadêmica",
    "NO_REGIAO": "Região",
    "SG_UF": "Unidade da Federação",
    "IN_CAPITAL": "Curso na Capital",
    "IN_GRATUITO": "Curso Gratuito",
    "IN_COMUNITARIA": "Instituição Comunitária",
    "IN_CONFESSIONAL": "Instituição Confessional",
    "CO_CURSO": "Código do Curso",
    "NO_CURSO": "Nome do Curso",
}


def pretty(col: str) -> str:
    return NOMES.get(col, col)


# ---------- rótulos legíveis (apenas para leitura/plots) ----------
MAPAS = {
    "TP_REDE": {1: "Pública", 2: "Privada"},
    "TP_CATEGORIA_ADMINISTRATIVA": {
        1: "Federal", 2: "Estadual", 3: "Municipal",
        4: "Privada c/ fins lucr.", 5: "Privada s/ fins lucr.",
        6: "Privada s/ fins lucr.", 7: "Especial",
    },
    "TP_ORGANIZACAO_ACADEMICA": {
        1: "Universidade", 2: "Centro Universitário",
        3: "Faculdade", 4: "IF/CEFET", 5: "IF/CEFET",
    },
    "TP_GRAU_ACADEMICO": {
        1: "Bacharelado", 2: "Licenciatura",
        3: "Tecnológico", 4: "Bach. e Lic.",
    },
    "TP_MODALIDADE_ENSINO": {1: "Presencial", 2: "EAD"},
    "TP_NIVEL_ACADEMICO": {1: "Graduação", 2: "Sequencial"},
    "IN_GRATUITO": {0: "Não", 1: "Sim"},
    "IN_CAPITAL": {0: "Não", 1: "Sim"},
    "IN_COMUNITARIA": {0: "Não", 1: "Sim"},
    "IN_CONFESSIONAL": {0: "Não", 1: "Sim"},
}


def aplicar_rotulos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col, mapa in MAPAS.items():
        if col not in df.columns:
            continue
        s = df[col].astype(object)
        df[col] = s.map(mapa).fillna(s).astype("category")
    return df


# ---------- medidas univariadas ----------
def resumo_univariado(df: pd.DataFrame) -> pd.DataFrame:
    linhas = []
    n_total = len(df)
    for col in df.columns:
        s = df[col]
        n_validos = s.notna().sum()
        vc = s.value_counts(dropna=True)
        if vc.empty:
            continue
        p = vc / vc.sum()
        # Entropia de Shannon normalizada (0 a 1): 1 = uniforme entre categorias
        H = entropy(p, base=2)
        Hmax = np.log2(len(p)) if len(p) > 1 else 1
        H_norm = H / Hmax if Hmax > 0 else 0.0
        # Índice de Gini-Simpson (1 - sum p^2): diversidade
        gini = 1 - (p ** 2).sum()
        linhas.append({
            "variavel": col,
            "n_validos": int(n_validos),
            "pct_faltantes": round(100 * (n_total - n_validos) / n_total, 2),
            "n_categorias": int(s.nunique(dropna=True)),
            "moda": vc.index[0],
            "freq_moda": int(vc.iloc[0]),
            "pct_moda": round(100 * vc.iloc[0] / vc.sum(), 2),
            "entropia_shannon": round(H, 4),
            "entropia_normalizada": round(H_norm, 4),
            "gini_simpson": round(gini, 4),
        })
    return pd.DataFrame(linhas)


def freq_table(s: pd.Series) -> pd.DataFrame:
    vc = s.value_counts(dropna=False)
    pct = (vc / vc.sum() * 100).round(2)
    return pd.DataFrame({"frequencia": vc, "percentual": pct})


# ---------- gráficos ----------
def plot_univariado(s: pd.Series, titulo: str, caminho: Path, top: int = 20):
    vc = s.value_counts(dropna=False).head(top)
    fig, ax = plt.subplots(figsize=(9, max(3, 0.35 * len(vc) + 1)))
    vc.iloc[::-1].plot.barh(ax=ax, color="#4C72B0")
    ax.set_title(titulo)
    ax.set_xlabel("Frequência")
    ax.set_ylabel("")
    for i, v in enumerate(vc.iloc[::-1].values):
        ax.text(v, i, f" {v:,}".replace(",", "."), va="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(caminho, dpi=130)
    plt.close(fig)


def plot_bivariado(df: pd.DataFrame, var: str, grupo: str, caminho: Path, top: int = 20):
    ct = pd.crosstab(df[var], df[grupo])
    ordem = ct.sum(axis=1).sort_values(ascending=False).head(top).index
    ct = ct.loc[ordem]
    pct = ct.div(ct.sum(axis=0), axis=1) * 100  # % dentro de cada grupo
    nome_var = pretty(var)
    nome_grupo = pretty(grupo)
    fig, ax = plt.subplots(figsize=(10, max(3, 0.4 * len(ct) + 1)))
    pct.iloc[::-1].plot.barh(ax=ax)
    ax.set_title(f"{nome_var} por {nome_grupo} (% dentro de cada {nome_grupo})")
    ax.set_xlabel(f"% dentro de cada {nome_grupo}")
    ax.set_ylabel(nome_var)
    ax.legend(title=nome_grupo, loc="best")
    fig.tight_layout()
    fig.savefig(caminho, dpi=130)
    plt.close(fig)


def plot_heatmap(df: pd.DataFrame, var: str, grupo: str, caminho: Path, top: int = 25):
    ct = pd.crosstab(df[var], df[grupo])
    ordem = ct.sum(axis=1).sort_values(ascending=False).head(top).index
    ct = ct.loc[ordem]
    pct = ct.div(ct.sum(axis=0), axis=1) * 100
    nome_var = pretty(var)
    nome_grupo = pretty(grupo)
    fig, ax = plt.subplots(figsize=(7, max(4, 0.35 * len(pct) + 1)))
    im = ax.imshow(pct.values, aspect="auto", cmap="Blues")
    ax.set_xticks(range(pct.shape[1]))
    ax.set_xticklabels(pct.columns, rotation=30, ha="right")
    ax.set_yticks(range(pct.shape[0]))
    ax.set_yticklabels(pct.index)
    for i in range(pct.shape[0]):
        for j in range(pct.shape[1]):
            ax.text(j, i, f"{pct.values[i, j]:.1f}", ha="center", va="center",
                    fontsize=8, color="black")
    ax.set_title(f"{nome_var} × {nome_grupo}  (% dentro de cada {nome_grupo})")
    ax.set_xlabel(nome_grupo)
    ax.set_ylabel(nome_var)
    fig.colorbar(im, ax=ax, label="%")
    fig.tight_layout()
    fig.savefig(caminho, dpi=130)
    plt.close(fig)


# ---------- execução ----------
print("Carregando base...")
df = pd.read_pickle(PKL)
print(f"  shape: {df.shape}")

print("Aplicando rótulos legíveis...")
df = aplicar_rotulos(df)

print("Gerando resumo univariado...")
resumo = resumo_univariado(df)
resumo.to_csv(OUT / "resumo_univariado.csv", index=False, encoding="utf-8-sig")

print("Gerando tabelas e gráficos por variável...")
for col in df.columns:
    ft = freq_table(df[col])
    ft.to_csv(TAB / f"freq_{col}.csv", encoding="utf-8-sig")
    plot_univariado(df[col], f"Distribuição de {pretty(col)}", GRA / f"uni_{col}.png")

print("Gerando análises bivariadas contra TP_REDE...")
GRUPO = "TP_REDE"
for col in df.columns:
    if col == GRUPO:
        continue
    ct = pd.crosstab(df[col], df[GRUPO], dropna=False)
    ct.to_csv(TAB / f"crosstab_{col}_por_rede.csv", encoding="utf-8-sig")
    pct = (ct.div(ct.sum(axis=0), axis=1) * 100).round(2)
    pct.to_csv(TAB / f"crosstab_pct_{col}_por_rede.csv", encoding="utf-8-sig")
    plot_bivariado(df, col, GRUPO, GRA / f"bi_{col}_por_rede.png")
    if df[col].nunique(dropna=True) <= 30:
        plot_heatmap(df, col, GRUPO, GRA / f"heatmap_{col}_por_rede.png")

print(f"\nConcluído. Saídas em: {OUT}")
