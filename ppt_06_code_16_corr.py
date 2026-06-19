# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Mapa de calor (heatmap) de la matriz de correlación del dataset Wine

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv('data/wine.csv')
df.drop('Class',axis='columns', inplace=True)

correlation_mat = df.corr()

fig = plt.figure(figsize=(8,8))

sns.heatmap(correlation_mat, annot = True)
plt.tight_layout()
plt.show()
