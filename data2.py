import numpy as np
import pandas as pd
import os

# Directorio donde se encuentran los archivos CSV
csv_directory = './archive/'

# Función para combinar datos de múltiples archivos CSV
def generate_appliance_usage_data_from_csv(file_names, num_records, start_year, end_year):
    """
    Genera un conjunto de datos de uso de electrodomésticos a partir de archivos CSV.

    Args:
        file_names: Lista de nombres de archivos CSV.
        num_records: El número de registros a generar por archivo.
        start_year: Año de inicio.
        end_year: Año de finalización.

    Returns:
        Un conjunto de datos de Pandas con los datos de uso de electrodomésticos.
    """

    data_frames = []

    for file_name in file_names:
        # Cargar datos del archivo CSV
        file_path = os.path.join(csv_directory, file_name)
        data = pd.read_csv(file_path, parse_dates=["timestamp"], index_col="timestamp")

        # Re-muestrear los datos para obtener num_records registros
        data_resampled = data.resample("H").mean()  # Muestreo por hora
        data_sample = data_resampled.sample(n=num_records, replace=True)

        # Generar fechas y horas
        date_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='H')
        date_samples = np.random.choice(date_range, num_records)

        # Convertir las fechas a objetos Timestamp y luego obtener la hora
        date_samples = pd.to_datetime(date_samples)
        data_sample['Fecha'] = date_samples
        data_sample['Hora'] = date_samples.hour

        data_frames.append(data_sample)

    # Combinar los DataFrames de todos los electrodomésticos
    combined_data = pd.concat(data_frames, ignore_index=True)

    # Generar columnas adicionales para probabilidad de fallo y reporte de fallo
    combined_data['Probabilidad de fallo'] = np.random.rand(len(combined_data))
    combined_data['Reporte de fallo'] = np.random.randint(0, 2, size=len(combined_data))

    return combined_data

# Generar un conjunto de datos combinado a partir de los archivos CSV
num_records_per_appliance = 50000  # 1 millón
start_year = 2019
end_year = 2023

file_names = [
    'dishwasher_53.csv',
    'boiler_226.csv',
    'air_purifier_293.csv',
    'sound_system_252.csv',
    '3D_printer_29.csv',
    'coffee_54.csv',
]

combined_df = generate_appliance_usage_data_from_csv(file_names, num_records_per_appliance, start_year, end_year)

# Guardar el conjunto de datos en un archivo CSV
combined_df.to_csv("combined_appliance_data1.csv", index=False)
