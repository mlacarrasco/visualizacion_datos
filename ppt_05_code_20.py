# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Gráfico de torta desde una Serie con colores y porcentajes personalizados

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

se = pd.Series(  np.random.rand(4), 
                 index = ["a", "b", "c", "d"], 
                 name = "Serie")

print(se)

se.plot.pie( labels=["AA", "BB", "CC", "DD"],
             colors=["r", "g", "b", "c"],
             autopct="%.2f",
             fontsize=20,
             figsize=(8,6))


plt.show()  
