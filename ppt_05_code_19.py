import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame( np.random.rand(4, 2), 
                 index = ["a", "b", "c", "d"],
                 columns = ["x", "y"] )

print(df)

df.plot.pie(subplots=True, figsize=(8, 4))
plt.show()
