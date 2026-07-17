# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Cálculo manual del test de Grubbs con scipy.stats para detectar outliers univariados

import numpy as np
from scipy import stats
from math import sqrt


def grubbs_crit(n, alpha=0.05):
    t = stats.t.ppf(1 - alpha/(n), n-2)
    return ((n-1)/sqrt(n)) * sqrt(t**2 / (n-2 + t**2))

data = np.array([5, 14, 15, 15, 19, 17, 16, 20, 22, 8, 21, 28, 11, 9, 29, 40])

# Grubbs secuencial
vals = data.copy()
outliers = []
while len(vals) > 2:
    n = len(vals)
    G = np.abs(vals - vals.mean()) / vals.std(ddof=1)
    i = G.argmax()
    if G[i] > grubbs_crit(n, 0.05):
        outliers.append(vals[i])
        vals = np.delete(vals, i)
    else:
        break

print("outliers:", outliers)   # [40]

