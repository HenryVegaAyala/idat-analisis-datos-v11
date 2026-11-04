import pandas as pd
import scipy.stats as st

df = pd.read_csv("tiempos.csv")

tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
electrica = df[df["vehiculo"] == "Electrica"]["minutos"]

print(f"Tiempo promedio del vehículo tradicional: {tradicional.mean()}")
print(f"Tiempo promedio del vehículo eléctrico: {electrica.mean()}")

ic_tradicional = st.t.interval(confidence=0.95, df=len(tradicional) - 1, loc=tradicional.mean(), scale=st.sem(tradicional))
print(f"Intervalo de confianza del 95% para el vehículo tradicional: {ic_tradicional[0]:.2f}, {ic_tradicional[1]:.2f}")

ic_electrica = st.t.interval(confidence=0.95, df=len(electrica) - 1, loc=electrica.mean(), scale=st.sem(electrica))
print(f"Intervalo de confianza del 95% para el vehículo eléctrico: {ic_electrica[0]:.2f}, {ic_electrica[1]:.2f}")

respuesta = st.ttest_ind(tradicional, electrica)
print(f"Valor p de la prueba t: {respuesta.pvalue:.4f}")

if respuesta.pvalue < 0.05:
    print("Se rechaza la hipótesis nula: hay una diferencia significativa entre los tiempos de los vehículos.")
else:
    print("No se rechaza la hipótesis nula: no hay una diferencia significativa entre los tiempos de los vehículos.")