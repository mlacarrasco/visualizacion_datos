# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Anotación específica de Chile con flecha sobre el scatter plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch

def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

colorbar ={"Africa":'k', "Asia":'y', "North America":'r', "Europe":'b', "Oceania":'g', "South America":'m'} 
markerlist =['.','^', '+', 's', 's', '*'] 
continents =["Africa", "Asia", "North America", "Europe", "Oceania", "South America"] 

fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

fig, ax = plt.subplots(figsize=(8,8))

label = "Chile"
ids = df.loc[df["Pais"]=="Chile"]
xs = ids["TasaFertilidad"].iloc[0]
ys = ids["IngresoPerCapita"].iloc[0]

ax.annotate(label,
            xy=(xs, ys),                    # el punto a ser etiquetado
            xytext=(100, 100),              # distancia del texto al punto
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->",  # estilo de la flecha
                            color='black',
                            lw=1.5,connectionstyle="arc3,rad=0.2"),
            ha='center',
            fontsize=15)

ax.grid()
ax.yaxis.set_major_formatter(fmtr)
for i in range(len(continents)):
  df_sel= df[df['Continente']==continents[i]]
  x = df_sel['TasaFertilidad']
  y = df_sel['IngresoPerCapita']
  ax.scatter(x,y, color=df_sel['Continente'].replace(colorbar), marker='.',label=continents[i], s=50)
 
ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')
ax.legend()

plt.show()