import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

date = pd.read_csv('Distance.txt')
cabeza = date.columns.tolist()
head=int(cabeza[0])

plt.hist(datos, bins=10, edgecolor='black')
y= datos.max().max()
plt.xlim(0, y+0.01) 
print(datos.max().max())
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title(f'Histograma de las distancias entre puntos con dimencion: {head}')

plt.show()
