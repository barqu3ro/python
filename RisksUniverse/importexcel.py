import pandas as pd
import json

# Cargar el archivo Excel
excel_file = "Universo de riesgos.xlsx"
sheet_name = "Mapa de Riesgos Auditoría de TI"
column_name = "Riesgo"

# Cargar los datos desde la hoja especificada
data_frame = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])

# Convertir los datos de la columna en una lista
data_list = data_frame[column_name].tolist()

# Crear una lista de diccionarios en formato JSON
json_data = [{"valor": item} for item in data_list]

# Guardar el JSON en un archivo
output_file = "output.json"

with open(output_file, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("Datos convertidos y guardados en el archivo:", output_file)
