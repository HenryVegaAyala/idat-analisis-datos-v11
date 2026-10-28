import pandas as pd

df = pd.read_csv("data/facturacion.csv")

print(df)
print("*" * 100)

resultado = df.dropna()
print(resultado)
print("*" * 100)

resultado = df.dropna(subset=["monto_total"])
print(resultado)
