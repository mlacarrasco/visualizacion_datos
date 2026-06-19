# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Scatter plot con marcador y color personalizados

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

x = df['TasaFertilidad']
y = df['IngresoPerCapita']

fig = plt.figure(figsize=(8,8))
plt.grid( alpha = 0.3)

plt.scatter(x, y, color='g', s=100, marker='+' )

plt.xlabel('Tasa de Fertilidad')
plt.ylabel('Ingreso per Cápita')
plt.show()
