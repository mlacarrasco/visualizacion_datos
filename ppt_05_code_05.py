# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Barras con índice de texto como etiqueta del eje X

import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({"ages": [65, 61, 25, 22, 27]}, 
                    index = ["Pedro","Juan","Sofía","Ale","Raúl"])

plotdata.plot(kind="bar")
plt.show()