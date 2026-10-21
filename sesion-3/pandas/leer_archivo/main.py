import pandas as pd

# Leer archivo csv
df = pd.read_csv("ventas_vento_2026_csv.csv")
print(df)

print("-" * 100)

# Leer archivo excel
df_excel = pd.read_excel("ventas_vento_2026_excel.xlsx", sheet_name="otros")
print(df_excel)
