import pandas as pd
import glob

# Buscar todos los archivos .csv en la carpeta data
buscar_archivos = glob.glob("data/ventas_*.csv")

print(f"Se encontraron {len(buscar_archivos)} archivos CSV.")

# Definir una lista para almacenar los DataFrames
dataframes = []

# Iterar sobre los archivos encontrados y leer cada uno en un DataFrame
for archivo_encontrado in buscar_archivos:
    print(f"Procesando archivo: {archivo_encontrado}")
    df = pd.read_csv(archivo_encontrado)

    # Agregar el DataFrame a la lista
    dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
consolidado = pd.concat(dataframes, ignore_index=True)
respuesta = consolidado.sort_values(by=['fecha'], ascending=False)

respuesta.to_csv("output/consolidado.csv", index=False)
respuesta.to_excel("output/consolidado.xlsx", index=False)