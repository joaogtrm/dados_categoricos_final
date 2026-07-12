"""Conversão única do pickle (formato Python) para CSV, pra R ler nativo."""
import pandas as pd

df = pd.read_pickle("dados/base_categorica_2024.pkl")
df.to_csv("dados/base_categorica_2024.csv", index=False)
print(f"OK: {df.shape[0]} linhas, {df.shape[1]} colunas -> dados/base_categorica_2024.csv")