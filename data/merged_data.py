import pandas as pd

# 1. Cargar los archivos
base = pd.read_excel("data/Data+for+Figure+2.1+(2011–2024).xlsx", engine="openpyxl")
extra = pd.read_csv("data/education.csv")

# 2. Filtrar el CSV por años
extra = extra[extra['Time'].isin([2019, 2020, 2021, 2022, 2023, 2024])]

# 3. Renombrar columnas
extra.rename(columns={'Country Name': 'Country name', 'Time': 'Year',
                      'School enrollment, tertiary (% gross) [SE.TER.ENRR]': 'School enrollment, tertiary (% gross)',
                      'School enrollment, secondary (% gross) [SE.SEC.ENRR]': 'School enrollment, secondary (% gross)'}, inplace=True)

# Imprimir las columnas del DataFrame extra para depuración
print("Columnas en el DataFrame extra:")
print(extra.columns)

# 4. Seleccionar columnas del CSV
extra = extra[['Country name', 'Year', 'School enrollment, tertiary (% gross)', 'School enrollment, secondary (% gross)']]

# 5. Unir los archivos
merged = base.merge(extra, on=['Country name', 'Year'], how='left')

# 6. Filtrar filas nulas/puntos
merged = merged.dropna(subset=['School enrollment, tertiary (% gross)', 'School enrollment, secondary (% gross)'], how='all')
merged = merged[~((merged['School enrollment, tertiary (% gross)'] == '..') & (merged['School enrollment, secondary (% gross)'] == '...'))]

# 7. Guardar el resultado
merged.to_csv("data/merged_data.csv", index=False)

print("Archivos combinados y limpiados exitosamente. Guardado como data/merged_data.csv")

# 8. Cargar el archivo resultante y mostrar las primeras filas
df = pd.read_csv("data/merged_data.csv")
print(df.head())