"""Conta a quantidade de ofertas por Rede de Ensino (Pública vs Privada)."""
import pandas as pd
from pathlib import Path

PKL = Path(__file__).resolve().parent.parent / "dados" / "base_categorica_2024.pkl"

df = pd.read_pickle(PKL)
mapa = {1: "Pública", 2: "Privada"}
s = pd.to_numeric(df["TP_REDE"], errors="coerce").map(mapa)
vc = s.value_counts(dropna=False)
total = vc.sum()
print(f"Total de ofertas: {total:,}".replace(",", "."))
for nome, n in vc.items():
    print(f"  {nome}: {n:,} ({100*n/total:.2f}%)".replace(",", "."))
