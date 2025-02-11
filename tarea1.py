#Aurelio Reyes Sánchez.
#Ejercicio 1.
#Primero vamos a definir una función que te dice si una gráfica es conexa
from collections import deque
def es_conexa(grafica):
    
    visitados=set() #Definimos un conjunto y agregaremos todos los nodos que se está visitando

    visitados.add(0) #Le agregamos el primer elemento y desde este iremos visitando todos los nodos 

    queue = deque([0]) #Agregamos a la cola el primer elemento
    
    while queue:
         
        vertice=queue.popleft() #A la variable vertice le asignamos al primer valor de la cola 

        for i in range(len(grafica)):
            if grafica[vertice][i]==1 and i not in visitados:
                visitados.add(i)
                queue.append(i)
    
    if len(visitados) == len(grafica):
        return True
    else:
        return False

grafica1 = [
    [0, 1, 0, 0],  # Nodo 0 conectado a 1
    [1, 0, 0, 0]  # Nodo 1 conectado a 0
]
print(es_conexa(grafica1))