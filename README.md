# Visualización de Datos

Repositorio de códigos de ejemplo para el curso de Visualización de Datos. Los scripts están organizados por presentación (PPT) y cubren desde gráficos básicos de distribución hasta técnicas avanzadas de detección de valores atípicos (outliers).

---

## Instalación de dependencias

### Requisito previo

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### Instalar todos los paquetes

```bash
pip install matplotlib pandas numpy seaborn plotly scipy scikit-learn statsmodels outlier_utils
```

### Paquetes individuales

| Paquete PyPI | Módulo que se importa | Uso en el proyecto |
|---|---|---|
| `matplotlib` | `matplotlib`, `matplotlib.pyplot` | Gráficos base (histogramas, scatter, boxplot, etc.) |
| `pandas` | `pandas` | Lectura de CSV y manejo de DataFrames |
| `numpy` | `numpy` | Generación de datos y operaciones matriciales |
| `seaborn` | `seaborn` | Gráficos estadísticos (violinplot, heatmap, regplot) |
| `plotly` | `plotly`, `plotly.express` | Gráficos interactivos |
| `scipy` | `scipy.stats`, `scipy` | Estadística (regresión lineal, Chi-cuadrado, Q-Q plot) |
| `scikit-learn` | `sklearn.*` | MDS, KNN, LOF, DBSCAN, RANSAC, escalado de datos |
| `statsmodels` | `statsmodels.formula.api` | Regresión OLS con resumen estadístico |
| `outlier_utils` | `outliers` | Test de Grubbs para detección de outliers |

> **Nota:** el paquete `outlier_utils` se instala con ese nombre en PyPI, pero se importa en el código como `from outliers import smirnov_grubbs`.

---

## Descripción de los archivos

### PPT 04 — Distribuciones univariadas

Gráficos para visualizar cómo se distribuyen los valores de una variable: strip plots, boxplots, histogramas y violin plots.

| Archivo | Descripción |
|---|---|
| `ppt_04_code_01.py` | Strip plot (diagrama de puntos en una dimensión) sobre datos de compras |
| `ppt_04_code_02.py` | Boxplot básico con datos aleatorios |
| `ppt_04_code_03.py` | Boxplot con muesca (`notch=True`) para comparar medianas |
| `ppt_04_code_04.py` | Histograma simple con una distribución uniforme |
| `ppt_04_code_05.py` | Histograma con dos distribuciones superpuestas |
| `ppt_04_code_06.py` | Histograma interactivo con Plotly Express |
| `ppt_04_code_07.py` | Histograma comparativo con Plotly: dos distribuciones superpuestas con boxplot marginal (`marginal='box'`), opacidad y control de bins |
| `ppt_04_code_08.py` | Histograma interactivo con Plotly configurado para Google Colab |
| `ppt_04_code_09.py` | Violin plot de una sola variable con Seaborn |
| `ppt_04_code_10.py` | Violin plot de múltiples variables con Seaborn |
| `ppt_04_code_11.py` | Histograma simple con Matplotlib y control de número de bins |
| `ppt_04_code_12.py` | Histograma acumulativo continuo |
| `ppt_04_code_13.py` | Histograma acumulativo con estilo de escalera (`histtype='step'`) |

---

### PPT 05 — Gráficos de barras

Distintas formas de representar datos categóricos y comparativos mediante barras.

| Archivo | Descripción |
|---|---|
| `ppt_05_code_01.py` | Gráfico de barras simple con datos de lenguajes de programación |
| `ppt_05_code_02.py` | Barras agrupadas lado a lado con tres categorías |
| `ppt_05_code_03.py` | Barras apiladas (hombres y mujeres por grupo) |
| `ppt_05_code_04.py` | Gráfico de barras desde un DataFrame de Pandas |
| `ppt_05_code_05.py` | Barras con índice de texto como etiqueta del eje X |
| `ppt_05_code_06.py` | Barras múltiples con datos de tres años y etiquetas de ejes |
| `ppt_05_code_07.py` | Selección de una sola columna del DataFrame para graficar |
| `ppt_05_code_08.py` | Selección de dos columnas específicas del DataFrame |
| `ppt_05_code_09.py` | Rotación de etiquetas del eje X (`rotation=45`) |
| `ppt_05_code_10.py` | Barras horizontales (`kind='barh'`) |
| `ppt_05_code_11.py` | Barras apiladas (`stacked=True`) |
| `ppt_05_code_12.py` | Barras apiladas normalizadas al 100% |
| `ppt_05_code_13.py` | Barras apiladas normalizadas transpuestas (por año en vez de por persona) |
| `ppt_05_code_14.py` | Coloreo de barras según una variable categórica (género) |
| `ppt_05_code_15.py` | Leyenda personalizada con `Patch` para el coloreo por categoría |
| `ppt_05_code_16.py` | Posicionamiento de la leyenda dentro del gráfico |
| `ppt_05_code_17.py` | Leyenda posicionada fuera del área del gráfico con `bbox_to_anchor` |
| `ppt_05_code_18.py` | Aplicación de un estilo predefinido de Matplotlib (`fivethirtyeight`) |
| `ppt_05_code_19.py` | Gráfico de torta con subplots desde un DataFrame |
| `ppt_05_code_20.py` | Gráfico de torta desde una Serie con colores y porcentajes personalizados |
| `ppt_05_code_21.py` | Diagrama de Cleveland (dot plot) para comparar valores entre dos años |
| `ppt_05_code_22.py` | Diagrama de Cleveland con etiquetas de países en el eje Y |

---

### PPT 06 — Gráficos de dispersión y correlación

Visualización de relaciones entre dos variables numéricas, regresión y análisis de correlación.

| Archivo | Descripción |
|---|---|
| `ppt_06_code_01.py` | Scatter plot básico: tasa de fertilidad vs ingreso per cápita |
| `ppt_06_code_02.py` | Scatter plot con marcador y color personalizados |
| `ppt_06_code_03.py` | Scatter plot con formato personalizado del eje Y (valores en miles de dólares) |
| `ppt_06_code_04.py` | Coloreo de puntos por continente con leyenda manual usando `Patch` |
| `ppt_06_code_05.py` | Variante del anterior con paleta de colores mejorada para mayor contraste |
| `ppt_06_code_06.py` | Marcadores distintos por continente y leyenda automática |
| `ppt_06_code_07.py` | Anotación de cada punto con el nombre de su continente |
| `ppt_06_code_08.py` | Anotación específica de Chile con flecha y escala logarítmica |
| `ppt_06_code_09.py` | Ejes en escala logarítmica (base 2 y base 10) con anotación de Chile |
| `ppt_06_code_10.py` | Curva de regresión polinomial de grado 6 con Seaborn (`regplot`) |
| `ppt_06_code_11.py` | Regresión con leyenda que identifica la curva y los puntos |
| `ppt_06_code_12_sns.py` | Regresión lineal sobre datos transformados (log2 / log10) con Seaborn |
| `ppt_06_code_13_stats.py` | Regresión lineal con resumen estadístico completo usando `statsmodels` y `scipy` |
| `ppt_06_code_14_QQ.py` | Q-Q plot para verificar normalidad y curva de densidad teórica |
| `ppt_06_code_15_MDS.py` | Escalado multidimensional (MDS) para visualizar datos del dataset Wine en 2D |
| `ppt_06_code_16_corr.py` | Mapa de calor (heatmap) de la matriz de correlación del dataset Wine |
| `ppt_06_code_17.py` | Scatter plot con tamaño y color de puntos variables, con doble leyenda |
| `ppt_06_code_99_sns.py` | Regresión lineal sobre Norteamérica con anotación del valor R |

---

### PPT 07 — Detección de valores atípicos (Outliers)

Métodos estadísticos y de machine learning para identificar datos anómalos.

| Archivo | Descripción |
|---|---|
| `ppt_07_code_01_outlier.py` | Cálculo manual del test de Grubbs usando `scipy.stats` |
| `ppt_07_code_02_GRUBS.py` | Test de Grubbs con la librería `outlier_utils`: detección en ambos lados, mínimo y máximo |
| `ppt_07_code_03_CHI2.py` | Detección multivariada con distancia de Mahalanobis y elipse de confianza Chi-cuadrado con gradiente visual |
| `ppt_07_code_04_MULTIVAR.py` | Detección multivariada con Mahalanobis sobre datos sintéticos con visualización de outliers en rojo |
| `ppt_07_code_05_KNN_simple.py` | Implementación manual de KNN para calcular distancias promedio a vecinos cercanos |
| `ppt_07_code_06_KNN.py` | Detección de outliers con KNN usando `scikit-learn`: punto codo para elegir umbral |
| `ppt_07_code_07_LOF.py` | Detección con Local Outlier Factor (LOF): círculos proporcionales al score de anomalía |
| `ppt_07_code_08_DBSCAN.py` | Clustering con DBSCAN para identificar puntos de ruido como outliers |

---

### PPT 08 — Regresión robusta con RANSAC

Ajuste de modelos lineales resistentes a la presencia de outliers.

| Archivo | Descripción |
|---|---|
| `ppt_08_code_01_RANSAC.py` | RANSAC sobre datos reales (ozono vs temperatura): comparación visual entre regresión estándar y RANSAC |
| `ppt_08_code_02_plot_ransac.py` | RANSAC sobre datos sintéticos con outliers artificiales: comparación de coeficientes estimados |

---

## Datos

Los archivos CSV usados por los scripts se encuentran en la carpeta `data/`:

| Archivo | Descripción |
|---|---|
| `week6.csv` | Datos de compras por cliente |
| `tasa.csv` | Tasas por país para dos años (2019 y 2020) |
| `tasaFertilidad2019.csv` | Tasa de fertilidad por país (2019) |
| `tasaFertilidad2019vsGPD.csv` | Tasa de fertilidad vs ingreso per cápita por país y continente (2019) |
| `airquality.csv` | Calidad del aire: ozono y temperatura |
| `wine.csv` | Dataset de vinos con atributos químicos y clase |
