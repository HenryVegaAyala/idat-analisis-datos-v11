import pandas as pd

enero = pd.read_csv("data/ventas_enero.csv")
febrero = pd.read_csv("data/ventas_febrero.csv")

resultado = pd.concat([enero, febrero], ignore_index=True)

print(resultado)