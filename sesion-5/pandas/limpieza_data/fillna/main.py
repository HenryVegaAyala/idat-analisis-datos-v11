import pandas as pd

df = pd.read_csv("data/facturacion.csv")

print(df)
print("*" * 100)

resultado = df.fillna(0)
print(resultado)
print("*" * 100)

resultado = df.fillna("Sin data")
print(resultado)
print("*" * 100)

resultado = df["monto_total"].fillna(df["monto_total"].mean())
print(resultado)
print("*" * 100)
