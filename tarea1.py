#Aurelio Reyes Sánchez.
#Ejercicio 1.
#Primero vamos a definir una función que te dice si una gráfica es conexa
from collections import deque
def es_conexa(grafica):
    
    visitados=set() #Definimos un conjunto y agregaremos todos los nodos que se está visitando

    visitados.add(0) #Le agregamos el primer elemento y desde este iremos visitando todos los nodos 

    queue = deque([0]) #Agregamos a la cola el primer elemento
    
    while queue: #Corre mientras la pila tiene elementos
         
        vertice=queue.popleft() #A la variable vertice le asignamos al primer valor de la cola 

        for i in range(len(grafica)):
            if grafica[vertice][i]==1 and i not in visitados: #Verifica que hay un lazo entre los dos nodos y que no este agregado ya en el conjunto de visitados.
                visitados.add(i) #Lo agrega al conjunto
                queue.append(i) #Lo agrega a la cola
    
    if len(visitados) == len(grafica): #Verifica si la el tamaño del conjunto es el mismo que el da la grafica 
        return True #Si
    else:
        return False

grafica1 = [
    [0, 1, 0, 0],  
    [1, 0, 0, 0]  
]
print(es_conexa(grafica1))

#Vamos a definir una función que te regrese el arbol generador de una gráfica simple cualquiera

