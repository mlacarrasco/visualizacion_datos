# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Leyenda posicionada fuera del área del gráfico con bbox_to_anchor

import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({ 	"pies_2018":[40, 12, 10, 26, 36],    				   
							"pies_2019":[19, 8, 30, 21, 38],    
			   				"pies_2020":[10, 10, 42, 17, 37] },    
                          index=["Dad", "Mam", "Bro", "Sis", "Me"])

plotdata.plot(kind="bar", figsize=(10,5))

plt.legend(
    loc='upper left', 
	bbox_to_anchor=(1, 1),
	title="Año de consumo"
)

plt.title("Consumo de Pies en la familia")
plt.xlabel("Miembros de la familia")
plt.ylabel("Pies consumidos")
plt.tight_layout()
plt.show()

