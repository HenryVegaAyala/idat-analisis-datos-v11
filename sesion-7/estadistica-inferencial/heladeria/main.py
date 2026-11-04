import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Cargar los datos del archivo CSV
df = pd.read_csv("heladeria_gastos.csv")
datos_de_gastos = df["gasto"]

# 2. Calcular el intervalo de confianza del 95%
intervalo = st.t.interval(
    confidence=0.95, # Nivel de confianza del 95%
    df=len(datos_de_gastos) - 1, # Grados de libertad (n-1)
    loc=np.mean(datos_de_gastos), # Media o promedio de los gastos
    scale=st.sem(datos_de_gastos)# Error estándar de la media
)

limiter_inferior = intervalo[0]
limiter_superior = intervalo[1]

# 3. Imprimir el intervalo de confianza
print(f"Con un grado de confianza del 95%, el gasto promedio "
      f"se encuentra entre S/. {limiter_inferior:.2f} y"
      f" S/. {limiter_superior:.2f}")

# 4. Calcular el promedio de los gastos
promedio_gastos = np.mean(intervalo)
print(f"El gasto promedio de los clientes es de S/. {promedio_gastos:.2f}")

# 5. Calcular el margen de error
margen_de_error = (limiter_superior - promedio_gastos)
print(f"El margen de error es de S/. {margen_de_error:.2f}")