import pandas as pd

df = pd.read_csv("data/facturacion.csv")

print(df.duplicated()) # Me retorna True o False si hay duplicados

resultado = df.drop_duplicates()
print(resultado)
