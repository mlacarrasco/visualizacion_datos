# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Barras apiladas normalizadas transpuestas (comparación por año)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plotdata = pd.DataFrame({ 	"pies_2018":[40, 12, 10, 26, 36],    				   
						  	"pies_2019":[19, 8, 30, 21, 38],    
			   				"pies_2020":[10, 10, 42, 17, 37] },    
                          index=["Dad", "Mam", "Bro", "Sis", "Me"])

plotdata = plotdata.transpose()

sumcol = np.sum(plotdata.values, axis=1)
plotdata = plotdata.divide(sumcol, axis=0)
plotdata.plot(kind="bar", stacked= True)

plt.title("Consumo de Pies por Año")
plt.xlabel("Año")
plt.ylabel("Pies Consumidos (%)")
plt.tight_layout()
plt.show()




