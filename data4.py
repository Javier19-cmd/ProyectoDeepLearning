import numpy as np
import pandas as pd
import os 

file_names = [
    "washing_machine_343.csv",
    "internet_router_295.csv",
    "vacuum_254.csv",
    "washing_machine_32.csv",
    'dishwasher_53.csv',
    'boiler_226.csv',
    'air_purifier_293.csv',
    'sound_system_252.csv',
    '3D_printer_29.csv',
    'coffee_54.csv',
    'phone_charger_282.csv',
    'fridge_207.csv',
    'radiator_309.csv',
    'dehumidifier_310.csv',
    'fridge_317.csv',
    'micro_wave_oven_314.csv',
    'laptop_289.csv',
    'tv_290.csv',
    'vacuum_236.csv',
    'screen_302.csv',
    'dehumidifier_322.csv',
    'solar_panel_325.csv',
    'screen_146.csv',
    'washing_machine_157.csv',
    'fan_215.csv',
    'air_conditioner_222.csv',
    'laptop_64.csv',
    'coffee_37.csv',
    'washing_machine_52.csv',
    'computer_44.csv',
    'boiler_233.csv',
    'micro_wave_oven_147.csv',
    'printer_286.csv',
    'fridge_284.csv',
    'coffee_97.csv',
    'fridge_98.csv',
    'washing_machine_135.csv',
    'internet_router_131.csv',
    'dryer_219.csv',
    'boiler_217.csv',
    'washing_machine_218.csv',
    'freezer_249.csv'
]

csv_directory = './archive/'

# Leer los archivos CSV y extraer la columna 'power'
power_data = []
for file_name in file_names:
    # Asegúrate de unir el directorio con el nombre del archivo
    file_path = os.path.join(csv_directory, file_name)
    df = pd.read_csv(file_path)
    power_data.extend(df['power'].tolist())

# Generar datos de uso de electrodomésticos

def generate_appliance_usage_data(num_records, start_year, end_year, power_data):
    """
    Genera un conjunto de datos de uso de electrodomésticos.

    Args:
        num_records: El número de registros a generar.
        start_year: Año de inicio.
        end_year: Año de finalización.
        power_data: Datos de potencia para usar como referencia.

    Returns:
        Un conjunto de datos de Pandas con los datos de uso de electrodomésticos.
    """

    # Generar fechas y horas
    date_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='H')
    dates = date_range[np.random.choice(len(date_range), num_records, replace=True)]
    hours = dates.hour

    # Generar datos de uso basados en 'power_data'
    watts_used = np.random.choice(power_data, size=num_records)

    # Generar un porcentaje de uso basado en la hora
    # Por ejemplo, puedes hacer que el uso sea más alto durante el día y disminuya por la noche
    usage_percentage = np.where((hours >= 8) & (hours <= 20), 90, 10)

    # Generar la probabilidad y el reporte de fallos
    probability_of_failure = np.random.rand(num_records)
    
    # Aquí generamos el reporte de fallos basado en la probabilidad generada
    report_of_failure = np.random.binomial(1, probability_of_failure)

    # Generando un porcentaje de fallo basado en la hora
    def generate_failure_percentage(hours):
        # La siguiente fórmula es solo un ejemplo y se puede ajustar según tus necesidades
        failure_percentage = (np.sin(hours / 24 * 2 * np.pi) + 1) * 25  # Variación diaria
        return failure_percentage

    # Ejemplo de uso:
    failure_percentages = generate_failure_percentage(hours)

    # Crear el DataFrame
    data = {
        "Fecha": dates,
        "Hora": hours,
        "Watts usados": watts_used,
        "Porcentaje de uso": usage_percentage,
        "Probabilidad de fallo": probability_of_failure,
        "Porcentaje de fallos": failure_percentages,
        "Reporte de fallo": report_of_failure,
    }

    df = pd.DataFrame(data)

    return df

# Generar un conjunto de datos de aproximadamente 3 millones de registros
num_records = 500_000  # 3 millones
start_year = 2019
end_year = 2023

df = generate_appliance_usage_data(num_records, start_year, end_year, power_data)

# Guardar el conjunto de datos en un archivo CSV
df.to_csv("appliance_usage_data1.csv", index=False)