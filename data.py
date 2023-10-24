import numpy as np
import pandas as pd

# Generar datos de uso de electrodomésticos

def generate_appliance_usage_data(num_records, start_year, end_year):
    """
    Genera un conjunto de datos de uso de electrodomésticos.

    Args:
        num_records: El número de registros a generar.
        start_year: Año de inicio.
        end_year: Año de finalización.

    Returns:
        Un conjunto de datos de Pandas con los datos de uso de electrodomésticos.
    """

    # Generar fechas y horas
    date_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='H')
    dates = date_range[np.random.choice(len(date_range), num_records, replace=True)]
    hours = dates.hour

    # Generar datos de uso
    watts_used = np.random.randint(100, 1000, size=num_records)
    probability_of_failure = np.random.rand(num_records)
    report_of_failure = np.random.randint(0, 2, size=num_records)

    # Crear el DataFrame
    data = {
        "Fecha": dates,
        "Hora": hours,
        "Watts usados": watts_used,
        "Probabilidad de fallo": probability_of_failure,
        "Reporte de fallo": report_of_failure
    }
    df = pd.DataFrame(data)

    return df

# Generar un conjunto de datos de aproximadamente 3 millones de registros
num_records = 3_000_000  # 3 millones
start_year = 2019
end_year = 2023

df = generate_appliance_usage_data(num_records, start_year, end_year)

# Guardar el conjunto de datos en un archivo CSV
df.to_csv("appliance_usage_data.csv", index=False)
