# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Scatter plot con tamaño y color de puntos variables y doble leyenda

import matplotlib.pyplot as plt
import numpy as np

#generamos datos aleatorios para el scatter plot
N = 405
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 300, size=N)

# las variables c y s se utilizan para asignar colores y 
# tamaños a los puntos del scatter plot, respectivamente
fig, ax = plt.subplots(figsize=(8,8))
scatter = ax.scatter(x, y, marker='.', s=s, c=c)

ax.grid(alpha =0.3)

# el * sirve para desempaquetar los elementos de la tupla que devuelve scatter.legend_elements() 
# y pasarlos como argumentos a ax.legend()
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Clases")

# agregamos la primera leyenda al gráfico para que no se sobreescriba con la segunda
ax.add_artist(legend1)

# legend_elements devuelve una tupla con dos listas: la primera contiene 
# los objetos de la leyenda (en este caso, los puntos del scatter plot) y 
# la segunda contiene las etiquetas correspondientes a cada objeto de la leyenda 
# (en este caso, las clases representadas por los colores de los puntos).
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)

legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")
plt.show()
