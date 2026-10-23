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