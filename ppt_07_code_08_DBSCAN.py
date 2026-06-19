# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Clustering con DBSCAN para identificar puntos de ruido como outliers

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Lectura de los datos
df = pd.read_csv('data/airquality.csv')
# Seleccionamos dos columnas
data_df = df[['Ozone', 'Temp']].dropna()

data_df = StandardScaler().fit_transform(data_df)
db = DBSCAN(eps=0.5, min_samples=5).fit(data_df)
labels = np.array(db.labels_)

fig, ax = plt.subplots()
for i in set(labels):
    index= labels==i
    ax.scatter(data_df[index,0], data_df[index,1], cmap='jet')
    
plt.show()
    
