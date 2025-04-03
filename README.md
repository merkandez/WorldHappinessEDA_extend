# 🌍 World Happiness EDA — Análisis Colaborativo

Este proyecto realiza un análisis exploratorio de datos (EDA) basado en el informe mundial de felicidad, con el objetivo de identificar los factores que más influyen en la percepción de bienestar en distintos países.

Se ha desarrollado de forma colaborativa, combinando análisis visual, estadístico y pruebas de hipótesis. El trabajo parte de una base individual y se amplía con secciones extendidas en equipo para profundizar en patrones y relaciones relevantes.

---

## 📁 Estructura del proyecto

```
📂 data/             # Dataset original
📂 notebooks/        # Análisis completo en Jupyter Notebook
📂 reports/          # Informe ejecutivo final en PDF y md
requirements.txt     # Dependencias del proyecto
README.md            # Este documento
```

---

## 🚀 Cómo usar este proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/merkandez/WorldHappinessEDA_extend.git
   cd WorldHappinessEDA_extend
   ```

2. Activa el entorno virtual (recomendado con `uv`):
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. Abre el notebook en VS Code o Jupyter Lab y sigue el análisis paso a paso.

---

## 🔧 Instalación rápida con pip (alternativa a uv)

Si no utilizas `uv`, puedes instalar manualmente las dependencias principales con:

```bash
pip install pandas numpy matplotlib seaborn plotly openpyxl
pip install -U nbformat
```

Esto te permitirá ejecutar correctamente el análisis completo en Jupyter o VS Code.

---

## 🔁 Guía base de análisis EDA

El análisis se estructura en fases reutilizables:

### 🔹 1. Exploración inicial
- Carga y revisión del dataset con pandas
- Identificación de tipos de variables y nulos

### 🔹 2. Limpieza de datos
- Eliminación de duplicados y valores faltantes
- Conversión de tipos y selección de años válidos (2019–2024)

### 🔹 3. Análisis univariado y multivariable
- Histogramas, boxplots, heatmaps, correlaciones, regresiones
- Visualizaciones: `seaborn`, `matplotlib`, `plotly`

### 🔹 4. Visualización avanzada
- 🌍 Mapas mundiales interactivos por año (`plotly.choropleth`)
- 📈 Gráfico comparativo de evolución por país (2011–2024)

---

## 📊 Sección Extendida – Pruebas de Hipótesis y Análisis Complementarios

Se ha ampliado el proyecto con nuevas secciones orientadas a validar hipótesis estadísticas y explorar relaciones visuales relevantes:

### 1. **Nivel educativo y bienestar**
> Hipótesis: la educación, medida a través de indicadores externos, tiene correlación con la puntuación de felicidad.

### 2. **Inflación y percepción de felicidad**
> Hipótesis: la inflación está inversamente relacionada con los niveles de felicidad registrados por país.

Se han aplicado pruebas como:
- **t de Student**
- **ANOVA**
- **Pruebas de correlación (Pearson, Spearman)**
- **Mann-Whitney U** y **Tukey HSD**

📁 Referencias y ejemplos completos en: `/notebooks/hypothesis_testing.ipynb`

---

### 📈 Resumen adicional: Regresión entre esperanza de vida y apoyo social

Se ha añadido un análisis de regresión lineal entre los factores:
- `Healthy life expectancy`
- `Social support`

Y su relación conjunta con el índice de felicidad (`Ladder score`).  
Este bloque busca mostrar gráficamente cómo influyen de forma combinada dos dimensiones sociales clave en el bienestar general.

---

## 📄 Informe final

Resumen ejecutivo en:

```
📁 reports/World_Happiness_Executive_Summary_FINAL.md
📁 reports/World_Happiness_Executive_Summary_FINAL.pdf
```

---

## 👥 Contribuidores

- **Anca Bacria**  
  [![GitHub](https://img.shields.io/badge/-@abac0-181717?style=flat&logo=github&logoColor=white)](https://github.com/a-bac-0)

- **Andreína Suescum**  
  [![GitHub](https://img.shields.io/badge/-@mariasuescum-181717?style=flat&logo=github&logoColor=white)](https://github.com/mariasuescum)

- **Alla Haruntyunyan**  
  [![GitHub](https://img.shields.io/badge/-@alharuty-181717?style=flat&logo=github&logoColor=white)](https://github.com/alharuty)

- **Mariela Adimari**  
  [![GitHub](https://img.shields.io/badge/-@marieadi-181717?style=flat&logo=github&logoColor=white)](https://github.com/marie-adi)

- **César Mercado**  
  [![GitHub](https://img.shields.io/badge/-@merkandez-181717?style=flat&logo=github&logoColor=white)](https://github.com/merkandez)

---

## ✨ Herramientas utilizadas

- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
- `scipy.stats`, `statsmodels` (pruebas de hipótesis)
- `JupyterLab` + VS Code

---

## 📚 Créditos

Este trabajo ha sido realizado como ejercicio formativo en análisis de datos.  
El objetivo es desarrollar un flujo completo de análisis con Python, aplicando visualización, estadística, pruebas de hipótesis y presentación ejecutiva de resultados.
