# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Gráfico de barras desde un DataFrame de Pandas

import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({"ages": [65, 61, 25, 22, 27]})

plotdata.plot(kind="bar")
plt.show()
