# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Detección multivariada con Mahalanobis sobre datos sintéticos con visualización de outliers

import numpy as np
import random
import matplotlib.pyplot as plt

from scipy.stats import chi2
from sklearn.datasets import make_blobs
from pandas import DataFrame

r_seed = 0

# Generar un cluster en 2D con un total de 1000 puntos
X, y = make_blobs(n_samples=1000, centers=1, n_features=2, random_state=r_seed)

# Generar puntos de ruido aleatorio, que pueden estar cerca o lejos del cluster
random.seed(r_seed)
random_pts = [[random.randint(-10, 10), random.randint(-10, 10)] for _ in range(50)]
X = np.append(X, random_pts, axis=0)

df = DataFrame(dict(x=X[:, 0], y=X[:, 1]))

# Calcular la media y la matriz de covarianza de todos los puntos
mean_values = X.mean(axis=0)
covariance_matrix = np.cov(X, rowvar=False)

# Identificar outliers usando la distancia de Mahalanobis al cuadrado, comparada
# con un umbral chi-cuadrado: la forma estadísticamente fundamentada de fijar
# un corte para datos normales multivariados, en lugar de un valor arbitrario de densidad
confidence_level = 0.999
chi2_threshold = chi2.ppf(confidence_level, df=X.shape[1])

inv_cov = np.linalg.inv(covariance_matrix)
diffs = X - mean_values
mahalanobis_sq = np.sum((diffs @ inv_cov) * diffs, axis=1)
outlier = mahalanobis_sq > chi2_threshold

# --- Visualización ---
fig, ax = plt.subplots(figsize=(8, 8))

# Puntos normales
ax.scatter(X[~outlier, 0], X[~outlier, 1],
           color='steelblue', alpha=0.6, s=30, label='Puntos normales')

# Outliers
ax.scatter(X[outlier, 0], X[outlier, 1],
           color='crimson', edgecolor='black', s=80, marker='X', label='Outliers')


ax.set_title(f'Detección de outliers ({outlier.sum()} encontrados de {len(X)} puntos)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.set_aspect('equal', adjustable='datalim')  # evita que la elipse se vea deformada
plt.show()

print(f"Se encontraron {outlier.sum()} outlier(s):")
print(X[outlier])