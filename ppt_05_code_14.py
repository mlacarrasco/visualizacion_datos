# Universidad Diego Portales
# Autor: Miguel Carrasco
# Ver: 1.0
# Fecha: 19/06/2026
# Descripción: Coloreo de barras según una variable categórica (género)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({ 	"edad":[48, 47, 10, 16, 18],    			               
						"genero":["M", "F","M", "F", "M"]},    
                      index=["Dad", "Mam", "Bro", "Sis", "Me"])


color = {"M": "#273c75", "F": "#44bd32"}

# el metodo .replace reemplaza los valores de la columna gender por 
# los colores definidos en el diccionario color
data["edad"].plot(kind="bar", color=data['genero'].replace(color))
plt.title("Estudio de la edad de la familia")
plt.tight_layout()
plt.legend()
plt.show()




