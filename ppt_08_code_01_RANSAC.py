# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Regresión robusta RANSAC sobre datos reales comparada con regresión lineal estándar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Lectura de los datos
df = pd.read_csv('data/airquality.csv')

# Seleccionamos dos columnas
df = df[['Ozone', 'Temp']]
df = df.dropna()
df = df.to_numpy()

X = df[:, 0].reshape(-1, 1)
y = df[:, 1]

# Ajustar una recta de regresión usando todos los datos
lr = linear_model.LinearRegression()
lr.fit(X, y)

# Ajustar un modelo lineal robusto usando el algoritmo RANSAC
ransac = linear_model.RANSACRegressor(min_samples=20)

ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

# Coeficientes beta0 y beta1 del modelo RANSAC
slope_ransac = ransac.estimator_.coef_[0]
intercept_ransac = ransac.estimator_.intercept_

# Predecir los datos usando los modelos estimados
line_X = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)

lw = 2
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharex=True, sharey=True)

# Panel izquierdo: datos originales, sin distinguir outliers
ax[0].scatter(X, y, color='gray', marker='o', s=25, alpha=0.7)
ax[0].set_title('Datos originales')
ax[0].set_xlabel('Ozono')
ax[0].set_ylabel('Temperatura')
ax[0].grid(alpha=0.3)

# Panel derecho: outliers/inliers detectados por RANSAC y ambas rectas ajustadas
ax[1].scatter(X[outlier_mask], y[outlier_mask], color='crimson', marker='o',
              s=35, alpha=0.8, label='Outliers')
ax[1].scatter(X[inlier_mask], y[inlier_mask], color='steelblue', marker='o',
              s=25, alpha=0.7, label='Inliers')
ax[1].plot(line_X, line_y_ransac, color='darkorange', linewidth=lw,
           label='Regresión RANSAC')
ax[1].plot(line_X, line_y, color='navy', linewidth=lw, linestyle='--',
           label='Regresión lineal estándar')
ax[1].set_title('RANSAC: inliers vs. outliers')
ax[1].set_xlabel('Ozono')
ax[1].grid(alpha=0.3)
ax[1].legend(loc='best', fontsize=9)

fig.suptitle('Comparación: regresión lineal estándar vs. RANSAC', fontsize=13)
plt.tight_layout()
plt.show()

print(f"Recta RANSAC: Temperatura = {slope_ransac:.3f} * Ozono + {intercept_ransac:.3f}")
print(f"Puntos clasificados como outliers: {outlier_mask.sum()} de {len(X)}")