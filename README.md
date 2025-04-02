# 🌍 World Happiness EDA

Este proyecto realiza un análisis exploratorio de datos (EDA) basado en el informe mundial de felicidad, con el objetivo de identificar los factores que más influyen en la percepción de bienestar en distintos países.

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
   git clone https://github.com/tuusuario/world-happiness-eda.git
   cd world-happiness-eda
   ```

2. Activa el entorno virtual (recomendado con `uv`):
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. Abre el notebook en VS Code o Jupyter Lab y sigue el análisis paso a paso.

---

## 🔁 Guía reutilizable de análisis EDA

Este proyecto sigue los pasos fundamentales de cualquier análisis exploratorio de datos. Puedes utilizar esta estructura como **modelo base** para otros proyectos, con ejemplos de funciones útiles en cada fase:

### 🔹 1. Carga y exploración inicial
- Leer datos: `pd.read_csv()`, `pd.read_excel()`
- Inspección general:
  - `.head()`, `.tail()`, `.sample()`
  - `.columns`, `.dtypes`, `.info()`, `.shape`, `.describe()`
- Objetivo: Comprender la estructura del dataset antes de transformarlo.

### 🔹 2. Limpieza de datos
- Detección y tratamiento de nulos:
  - `.isna().sum()`, `.dropna()`, `.fillna()`
- Eliminar duplicados: `.duplicated()`, `.drop_duplicates()`
- Conversión de tipos: `.astype()`
- Crear copia limpia: `df_limpio = df.copy()`

### 🔹 3. Análisis univariado
- Visualización individual de cada variable:
  - `sns.histplot()`, `sns.boxplot()`, `plt.hist()`
- Objetivo: Detectar sesgos, outliers y distribuciones relevantes.

### 🔹 4. Análisis multivariable
- Calcular correlaciones: `.corr()`
- Visualizar correlaciones: `sns.heatmap()`
- Comparar variables clave: `sns.scatterplot()`, `sns.regplot()`
- Objetivo: Detectar patrones entre factores y variable objetivo.

### 🔹 5. Conclusiones y documentación
- Registrar observaciones: Markdown en celdas del notebook
- Sintetizar hallazgos clave para informes
- Exportar a formatos entregables: `.md`, `.pdf`.

---

## 📄 Informe final

Consulta el resumen ejecutivo completo en:

```
📁 reports/World_Happiness_Executive_Summary.md
📁 reports/World_Happiness_Executive_Summary.pdf
```

Incluye resultados clave, visualizaciones y propuestas para ampliar el análisis en futuros proyectos.

---

## ✨ Créditos

Este proyecto fue realizado como ejercicio formativo para dominar el flujo de trabajo típico de un análisis EDA con Python, utilizando:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `Jupyter Notebooks`
