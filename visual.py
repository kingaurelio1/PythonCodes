import numpy as np
import matplotlib.pyplot as plt

# Definimos las probabilidades y valores del dado
valores = np.array([1, 2, 3, 4, 5, 6])
probabilidades = np.array([0.1, 0.2, 0.3, 0.2, 0.1, 0.1])

# Número de simulaciones
n_simulaciones = 10000
tamano_muestra = 30  # Número de lanzamientos por simulación

# Simulamos lanzamientos del dado
# Realizamos n_simulaciones y para cada simulación lanzamos el dado 'tamano_muestra' veces
lanzamientos = np.random.choice(valores, size=(n_simulaciones, tamano_muestra), p=probabilidades)

# Calculamos el promedio de cada simulación
promedios = lanzamientos.mean(axis=1)

# Graficamos la distribución de los promedios
plt.figure(figsize=(10, 6))
plt.hist(promedios, bins=30, density=True, alpha=0.6, color='g')

# Título y etiquetas
plt.title("Distribución de los Promedios de Lanzamientos de un Dado Sesgado (n=30)", fontsize=14)
plt.xlabel("Promedio de lanzamientos", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.grid(True)
plt.show()
