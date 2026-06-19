# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Q-Q plot para verificar normalidad y curva de densidad teórica

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

mu= 75
sigma = 6

#generamos datos con una distribución normal con media mu y desviación estándar sigma
s = np.random.normal(loc = mu, scale = sigma, size= 40)   
print(np.sort(s))

#generamos un grafico Q-Q plot para verificar si los datos siguen una distribución normal
stats.probplot(s, dist="norm", plot=plt)
plt.show()

# generamos un histograma de los datos y superponemos la curva de densidad 
# teórica de la distribución normal con media mu y desviación estándar sigma
count, bins, ignored = plt.hist(s, 14, density=True)

# ploteamos la curva de densidad teórica de la distribución normal 
# con media mu y desviación estándar sigma
plt.plot(bins, 
          1/(sigma*np.sqrt(2*np.pi)) * np.exp(- (bins-mu)**2/(2*sigma**2)),
          linewidth = 2, 
          color='r')

plt.show()

