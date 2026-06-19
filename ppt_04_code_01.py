# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Strip plot (diagrama de puntos en 1D) de datos de compras por cliente

import matplotlib.pyplot as plt
import numpy as np

#generamos datos al azar
data = np.random.normal(loc=100, scale=20, size=200)
my_range = np.ones((1, len(data)))*np.random.rand(len(data)) * 0.1 - 0.05

fig  = plt.figure(figsize=(10,2))

ax = fig.gca()
ax.get_yaxis().set_visible(False)

plt.scatter(data,my_range, color='blue', label='Compras', alpha=0.3)
plt.axhline(y=0, color='red', linestyle='--', label='Media', linewidth=0.5)
plt.ylim(-1,1)
plt.title("Distribución de datos")
plt.xlabel('Promedio de compras por cliente')
plt.show()
