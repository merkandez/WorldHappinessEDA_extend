🌍 World Happiness EDA — Análisis Colaborativo
Este proyecto realiza un análisis exploratorio de datos (EDA) basado en el informe mundial de felicidad, con el objetivo de identificar los factores que más influyen en la percepción de bienestar en distintos países.

Se ha desarrollado de forma colaborativa, combinando análisis visual, estadístico y pruebas de hipótesis. El trabajo parte de una base individual y se amplía con secciones extendidas en equipo para profundizar en patrones y relaciones relevantes.

📁 Estructura del proyecto
📂 data/             # Dataset original
📂 notebooks/        # Análisis completo en Jupyter Notebook
📂 reports/          # Informe ejecutivo final en PDF y md
📂 visualizations/   # Gráficos avanzados y mapas interactivos
requirements.txt     # Dependencias del proyecto
README.md            # Este documento
🚀 Cómo usar este proyecto
Clona el repositorio:

git clone https://github.com/tuusuario/world-happiness-eda.git
cd world-happiness-eda
Activa el entorno virtual (recomendado con uv):

uv venv
uv pip install -r requirements.txt
Abre el notebook en VS Code o Jupyter Lab y sigue el análisis paso a paso.

🔁 Guía base de análisis EDA
El análisis se estructura en fases reutilizables:

🔹 1. Exploración inicial
Carga y revisión del dataset con pandas
Identificación de tipos de variables y nulos
🔹 2. Limpieza de datos
Eliminación de duplicados y valores faltantes
Conversión de tipos y selección de años válidos (2019–2024)
🔹 3. Análisis univariado y multivariable
Histogramas, boxplots, heatmaps, correlaciones, regresiones
Visualizaciones: seaborn, matplotlib, plotly
🔹 4. Visualización avanzada
🌍 Mapa mundial interactivo por año (plotly.choropleth)
📈 Gráfico comparativo de evolución por país (2011–2024)
📊 Sección Extendida – Pruebas de Hipótesis
Se han añadido 3 bloques de análisis con pruebas de hipótesis, aplicando técnicas estadísticas clásicas para validar suposiciones con evidencia empírica:

1. Relación entre salud y felicidad
Hipótesis: la esperanza de vida saludable influye de forma significativa en la percepción de felicidad.

2. Nivel educativo y bienestar
Hipótesis: la educación, medida a través de indicadores externos, tiene correlación con la puntuación de felicidad.

3. [Nombre de la hipótesis 3 pendiente de definir]
📝 Completar aquí una vez definida la tercera línea de análisis.

Se han aplicado pruebas como:

t de Student
ANOVA
Pruebas de correlación (Pearson, Spearman)
Mann-Whitney U y Tukey HSD
Referencias y ejemplos completos en el documento /notebooks/hypothesis_testing.ipynb.

📄 Informe final
Resumen ejecutivo en:

📁 reports/World_Happiness_Executive_Summary_FINAL.md
📁 reports/World_Happiness_Executive_Summary_FINAL.pdf
👥 Contribuidores
🧑‍💻 [Nombre del integrante 1]
🧑‍💻 [Nombre del integrante 2]
🧑‍💻 [Nombre del integrante 3]
Completar con los nombres y enlaces a GitHub si procede

✨ Herramientas utilizadas
pandas, numpy, matplotlib, seaborn, plotly
scipy.stats, statsmodels (pruebas de hipótesis)
JupyterLab + VS Code
📚 Créditos
Este trabajo ha sido realizado como ejercicio formativo en análisis de datos.
El objetivo es desarrollar un flujo completo de análisis con Python, aplicando visualización, estadística y presentación ejecutiva de resultados.