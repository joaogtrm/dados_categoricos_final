"""
Lê o cadastro de cursos do Censo da Educação Superior 2024 (INEP),
seleciona apenas as variáveis categóricas relevantes ao estudo
e salva o resultado em um arquivo .pkl.

Obs.: o cadastro_ies não é utilizado porque todas as variáveis
selecionadas já estão presentes em cadastro_cursos (desnormalizadas).
"""

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
CURSOS_CSV = BASE / "dados" / "MICRODADOS_CADASTRO_CURSOS_2024.CSV"
SAIDA = BASE / "dados" / "base_categorica_2024.pkl"

VARS_SELECIONADAS = [
    # Agrupamento
    "TP_CATEGORIA_ADMINISTRATIVA",
    "TP_REDE",
    "IN_GRATUITO",
    # Áreas (alvo)
    "NO_CINE_AREA_GERAL",
    "NO_CINE_AREA_ESPECIFICA",
    "NO_CINE_AREA_DETALHADA",
    # Caracterização do curso
    "TP_GRAU_ACADEMICO",
    "TP_MODALIDADE_ENSINO",
    "TP_ORGANIZACAO_ACADEMICA",
    "TP_NIVEL_ACADEMICO",
    # Geográficas
    "NO_REGIAO",
    "SG_UF",
    "IN_CAPITAL",
    # Complementares (subgrupo privado)
    "IN_COMUNITARIA",
    "IN_CONFESSIONAL",
]

print("Lendo cadastro_cursos (apenas colunas selecionadas)...")
df = pd.read_csv(
    CURSOS_CSV,
    sep=";",
    encoding="latin1",
    usecols=VARS_SELECIONADAS,
    low_memory=False,
)
print(f"  shape: {df.shape}")

for c in df.columns:
    df[c] = df[c].astype("category")

print(df.dtypes)
print(df.head())

SAIDA.parent.mkdir(parents=True, exist_ok=True)
df.to_pickle(SAIDA)
print(f"\nArquivo salvo em: {SAIDA}")
