import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

df = pd.read_csv('dataset.txt')
print(df.info())

print("-" * 100)
print(df.describe())

print("-" * 100)
print(df["Store ID"].value_counts())

print("-" * 100)
print(df[["Total Price", "Store ID"]])

print("-" * 100)

filtrado = df["Store ID"] == 8091
print(df[filtrado])

filtrado_avanzado = (df["Store ID"] == 8091) & (df["Total Price"] > 100)

print(df[filtrado_avanzado])