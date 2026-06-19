# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Histograma interactivo con Plotly configurado para Google Colab

import pandas as pd
import plotly.express as px
import plotly

#importante: este codigo solo se muestra en colab, 
# por lo que se debe configurar el renderizador de 
# plotly para colabplotly.io.renderers.default = 'colab'


plotly.io.renderers.default = 'colab'

import numpy as np

col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age':col_1,
                   'Height': col_2})

fig = px.histogram(df, x="Age",title='Histograma del atributo edad')
fig.show()
