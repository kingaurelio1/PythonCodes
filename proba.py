import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros de la distribución normal
mu = 75  # Edad media
sigma = 10  # Desviación estándar

# Crear un rango de edades (de 40 a 110 años)
x = np.linspace(40, 110, 1000)

# Obtener las probabilidades correspondientes usando la distribución normal
y = norm.pdf(x, mu, sigma)

# Graficar
plt.plot(x, y, label='Distribución Normal', color='blue')
plt.fill_between(x, y, alpha=0.2, color='blue')

# Etiquetas y título
plt.title('Distribución de Edad de Muerte')
plt.xlabel('Edad')
plt.ylabel('Probabilidad')

# Mostrar la gráfica
plt.show()