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


ax.yaxis.set_major_formatter(fmtr)
for i in range(len(continents)):
  df_sel= df[df['Continente']==continents[i]]
  x = df_sel['TasaFertilidad']
  y = df_sel['IngresoPerCapita']
  ax.scatter(x,y, color=df_sel['Continente'].replace(colorbar), marker='.',label=continents[i], s=50)
 
ids = df.loc[df["Pais"]=="Chile"]
xs =ids["TasaFertilidad"].iloc[0]
ys = ids["IngresoPerCapita"].iloc[0]

plt.annotate("Chile", # este es el texto
            (xs,ys), # estas son las coordenadas del punto
            textcoords="offset points", # cómo posicionar el texto
            xytext=(50,50), # distancia del texto al punto (x,y)
            size = 15,
            arrowprops=dict(arrowstyle="->", color='black', lw=1.5),
            ha='left',
            fontsize=15) # alineación horizontal: left, right o center

ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer (log 2)')
ax.set_ylabel('Promedio de per cápita, en miles de US$ (log 10)')
ax.legend()
ax.set_xscale('log', base=2)
ax.set_yscale('log', base=10)

ax.grid(alpha=0.3, which="both", ls="-")

plt.show()