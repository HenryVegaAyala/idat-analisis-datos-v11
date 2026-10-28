import pandas as pd
import glob
from pathlib import Path

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

# Ubicación de la carpeta de salida en el mismo directorio que el script
carpeta_salida = Path(__file__).resolve().parent / "output"
carpeta_salida.mkdir(parents=True, exist_ok=True)
respuesta.to_csv(carpeta_salida / "consolidado.csv", index=False)
respuesta.to_excel(carpeta_salida / "consolidado.xlsx", index=False)

# Ubicación de la carpeta de salida en otro directorio
carpeta_salida_documentos = Path.home() / "Documents" / "output"
carpeta_salida_documentos.mkdir(parents=True, exist_ok=True)
respuesta.to_csv(carpeta_salida_documentos / "consolidado.csv", index=False)
respuesta.to_excel(carpeta_salida_documentos / "consolidado.xlsx", index=False)

