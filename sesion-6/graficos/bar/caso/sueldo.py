import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde un archivo CSV
data = pd.read_csv('salarios.csv')

empleado = data["nombre"]
sueldo = data["sueldo"]

plt.bar(empleado, sueldo, color="green")

plt.title("Empleado vs Sueldo")
plt.xlabel("Empleado")
plt.ylabel("Sueldo")

plt.show()