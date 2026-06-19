# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Regresión con leyenda que identifica la curva y los puntos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

df_sel = df[df['Continente']=='North America']
xs = df_sel['TasaFertilidad']
ys = df_sel['IngresoPerCapita']

fig, ax = plt.subplots(figsize=(8,8))
ax.grid(alpha=0.3)

p = sns.regplot(x = xs, y =ys, ci=None, order=6, label="Curva Regresion")

ax.scatter(xs, ys ,marker='o', color = 'r', s=30, label="Norteamerica")

ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')

plt.legend()
plt.show()

