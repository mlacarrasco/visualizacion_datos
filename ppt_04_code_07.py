import pandas as pd
import plotly.express as px
import numpy as np

np.random.seed(42)

col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age': col_1,
                   'Height': col_2})

# melt convierte las dos columnas en una sola, con una columna 'Variable'
# que indica a qué atributo pertenece cada valor
df_melt = df.melt(var_name='Variable', value_name='Valor')

print(df_melt)
fig = px.histogram(
    df_melt,
    x='Valor',
    color='Variable',
    barmode='overlay', #barmode: sirve para superponer las barras de los histogramas
    opacity=0.7,
    marginal='box',
    nbins=30,
    title='Histograma comparativo con distribución marginal'
)

fig.show()
