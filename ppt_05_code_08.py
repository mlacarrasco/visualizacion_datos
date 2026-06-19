# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Selección de dos columnas específicas del DataFrame

import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({ 	"pies_2018":[40, 12, 10, 26, 36],    				   
							"pies_2019":[19, 8, 30, 21, 38],    
							"pies_2020":[10, 10, 42, 17, 37] },    
                          index=["Dad", "Mam", "Bro", "Sis", "Me"])

plotdata[["pies_2018", "pies_2020"]].plot(kind="bar")

plt.title("Estudio de consumo de Pies en la familia en 2018 y 2020")
plt.xlabel("Miembros de la familia")
plt.ylabel("Pies consumidos")
plt.tight_layout()
plt.show()


