import pandas as pd

df = pd.read_csv("ventas.csv")

print(df.head())
print("-" * 100)

df["ingreso_total"] = df["cantidad"] * df["precio_unitario"]
print(df.head())