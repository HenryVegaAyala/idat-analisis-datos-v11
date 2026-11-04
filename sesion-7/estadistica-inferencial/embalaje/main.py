import pandas as pd
import scipy.stats as st

df = pd.read_csv("satisfaccion.csv")

grupo_a = df[df["embalaje"] == "A"]["puntuacion"]
grupo_b = df[df["embalaje"] == "B"]["puntuacion"]

print(f"Grupo A: {grupo_a.mean()}")
print(f"Grupo B: {grupo_b.mean()}")

resultado = st.ttest_ind(grupo_a, grupo_b)

print(f"Resultado de la prueba: {resultado.pvalue}")