# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Marcadores distintos por continente con leyenda automática

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

colorbar ={"Africa":'k', "Asia":'y', "North America":'r', "Europe":'b', "Oceania":'g', "South America":'m'} 
markerlist =['o','^', '+', 's', 's', '*'] 
continents =["Africa", "Asia", "North America", "Europe", "Oceania", "South America"] 


fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')


fig, ax = plt.subplots(figsize=(8,8))
ax.grid(alpha=0.3, linestyle='--')
ax.yaxis.set_major_formatter(fmtr)

# recorremos cada continente para graficar cada uno con un color y marcador diferente, 
# y para agregar una leyenda con el nombre de cada continente

for i in range(len(continents)):
  df_sel= df[df['Continente']==continents[i]]
  x = df_sel['TasaFertilidad']
  y = df_sel['IngresoPerCapita']
  ax.scatter(x,y, 
             color=df_sel['Continente'].replace(colorbar), 
             marker=markerlist[i],
             label=continents[i], 
             s=50,
             alpha=0.7)

ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')
ax.legend()



plt.show()