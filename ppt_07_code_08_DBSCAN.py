"""
 Universidad Diego Portales
 Facultad de Ingeniería y Ciencias
 Visualización de Datos

 
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (02/09/2019)

 
 Objetivo:
 1) Clustering de datos con DBSCAN
 2) Desplegar el resultado en un plot
 
    
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

df=pd.read_csv('data/week5.csv')   # lee los datos del archivo csv
df.dropna(subset=['op','ag'], inplace=True)
data_df = df[["op","ag"]]

data_df= StandardScaler().fit_transform(data_df)
db= DBSCAN(eps=0.5, min_samples=5).fit(data_df)
labels = np.array(db.labels_)

fig, ax = plt.subplots()
for i in set(labels):
    index= labels==i
    ax.scatter(data_df[index,1], data_df[index,0], cmap='jet')
    
plt.show()
    
