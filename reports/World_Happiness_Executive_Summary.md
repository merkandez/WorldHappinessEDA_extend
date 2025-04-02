# Informe ejecutivo – World Happiness Report (EDA)

## 1. Introducción

Este informe presenta los resultados de un análisis exploratorio de datos (EDA) basado en el *World Happiness Report*.  
El objetivo principal ha sido identificar los factores más asociados a la percepción de felicidad en distintos países, utilizando un enfoque visual, descriptivo y global.

Este trabajo representa la primera fase de un posible estudio más amplio y detallado sobre el bienestar global.

---

## 2. Alcance y metodología

Durante el análisis se han aplicado técnicas clásicas de EDA con Python, entre ellas:

- Carga, limpieza y estructuración del dataset (2019–2024)
- Análisis univariado de cada factor explicativo
- Estudio de correlaciones con el índice de felicidad (`Ladder score`)
- Visualización de tendencias mediante histogramas, heatmaps y scatterplots
- Redacción reflexiva de observaciones clave y relaciones detectadas

Este enfoque permite observar cómo varía la felicidad entre países y qué factores se asocian más directamente a ese nivel de bienestar percibido.

---

## 3. Principales hallazgos

- Los factores más correlacionados con la felicidad son:
  - **PIB per cápita (Log GDP)**: 0.69
  - **Apoyo social**: 0.69
  - **Esperanza de vida saludable**: 0.66
- La **libertad personal** y la **percepción de corrupción** también muestran relación positiva, aunque más moderada.
- La **generosidad**, aunque culturalmente valiosa, no presenta relación estadística significativa con la felicidad global.
- Las visualizaciones refuerzan estas correlaciones de forma clara.

Este análisis pone en evidencia que los factores económicos, sanitarios y sociales son los pilares del bienestar percibido a nivel país.

---

## 4. Vías para ampliación futura

Este informe se centra en el análisis descriptivo general, pero **abre múltiples posibilidades para desarrollar el estudio en fases siguientes**:

- **Análisis de evolución temporal por país**: observar cómo ha cambiado la felicidad a lo largo de los años.
- **Comparaciones regionales o culturales**: detectar patrones comunes según zonas geográficas.
- **Relación con eventos históricos concretos**: como crisis, pandemias o conflictos armados.
- **Modelado predictivo**: mediante regresión o machine learning para predecir el índice de felicidad.
- **Cruce con otros indicadores externos**: como educación, seguridad, gobernabilidad o igualdad.

---

## 5. Conclusión

Este proyecto demuestra el valor de un análisis exploratorio bien estructurado para **comprender la felicidad global a través de los datos**.

Aunque no se ha pretendido construir un modelo predictivo, los resultados obtenidos ofrecen una visión clara y visualmente comprensible de los factores clave.  
Este trabajo sienta las bases para posibles investigaciones futuras de carácter más profundo, comparativo o predictivo, en el ámbito del bienestar mundial.

---

🧪 Proyecto realizado como ejercicio formativo de análisis exploratorio de datos con Python.
