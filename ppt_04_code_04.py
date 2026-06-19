# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Histograma simple con una distribución uniforme

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rand_values = np.random.rand(50) * 100
df = pd.DataFrame({'data':rand_values })

ax = df.plot.hist(bins=12, alpha=0.5)

plt.show()
