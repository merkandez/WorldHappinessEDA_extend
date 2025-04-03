import pandas as pd

base = pd.read_excel("data/Data+for+Figure+2.1+(2011–2024).xlsx", engine="openpyxl")
extra = pd.read_csv("data/education.csv")

extra = extra[extra['Time'].isin([2019, 2020, 2021, 2022, 2023, 2024])]

extra.rename(columns={'Country Name': 'Country name', 'Time': 'Year',
                      'School enrollment, tertiary (% gross) [SE.TER.ENRR]': 'School enrollment, tertiary (% gross)',
                      'School enrollment, secondary (% gross) [SE.SEC.ENRR]': 'School enrollment, secondary (% gross)'}, inplace=True)

print("Columnas en el DataFrame extra:")
print(extra.columns)

extra = extra[['Country name', 'Year', 'School enrollment, tertiary (% gross)', 'School enrollment, secondary (% gross)']]

merged = base.merge(extra, on=['Country name', 'Year'], how='left')


merged = merged.dropna(subset=['School enrollment, tertiary (% gross)', 'School enrollment, secondary (% gross)'], how='all')
merged = merged[~((merged['School enrollment, tertiary (% gross)'] == '..') & (merged['School enrollment, secondary (% gross)'] == '...'))]


merged.to_csv("data/merged_data.csv", index=False)

print("Archivos combinados y limpiados exitosamente. Guardado como data/merged_data.csv")


df = pd.read_csv("data/merged_data.csv")
print(df.head())