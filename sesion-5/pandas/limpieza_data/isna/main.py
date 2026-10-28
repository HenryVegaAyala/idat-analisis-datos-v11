import pandas as pd

df = pd.read_csv("data/facturacion.csv")

resultado = df.isna().sum()

print(resultado)