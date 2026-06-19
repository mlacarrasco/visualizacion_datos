# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Gráfico de barras simple con popularidad de lenguajes de programación

import matplotlib.pyplot as plt

fig = plt.figure()

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]

plt.bar(langs,students)

plt.show()
