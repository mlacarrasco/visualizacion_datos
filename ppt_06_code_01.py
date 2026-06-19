# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Scatter plot básico de tasa de fertilidad vs ingreso per cápita

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

x = df['TasaFertilidad']
y = df['IngresoPerCapita']

fig = plt.figure(figsize=(8,8))
plt.grid(axis='both', linestyle='--', alpha=0.3)

plt.scatter(x, y, color='k')
plt.xlabel('Tasa de Fertilidad')
plt.ylabel('Ingreso per Cápita')
plt.show()
