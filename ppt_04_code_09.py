# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Violin plot de una sola variable con Seaborn

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")


col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age':col_1,
                   'Height': col_2})

# split: para mostrar ambas partes del violín por separado, 
# inner: para mostrar los cuartiles dentro del violín
ax = sns.violinplot(x=df['Height'], split= True, inner="quartile")

plt.show()
