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

#Vamos a definir una función que te regrese el arbol generador de una gráfica simple cualquiera
def arbol_generador(grafica):
    n = len(grafica)  # Número de nodos en el grafo
    visitado = [False] * n  # Lista para saber si un nodo ha sido visitado
    matriz_adyacencia = [[0] * n for _ in range(n)]  # Inicializamos la matriz de adyacencia

    def bfs(start):
        # Función para hacer BFS desde un nodo 'start'
        queue = deque([start])  # Cola de BFS
        visitado[start] = True  # Marcamos el nodo inicial como visitado
        subarbol = []  # Lista para almacenar las aristas del árbol generado en este componente
        
        while queue:
            vertice = queue.popleft()  # Extraemos el primer nodo de la cola
            
            # Exploramos los vecinos del nodo
            for vecino in range(n):
                if grafica[vertice][vecino] == 1 and not visitado[vecino]:
                    visitado[vecino] = True  # Marcamos el vecino como visitado
                    queue.append(vecino)  # Agregamos el vecino a la cola
                    subarbol.append((vertice, vecino))  # Agregamos la arista al árbol generador
                    
                    # Actualizamos la matriz de adyacencia para reflejar la arista
                    matriz_adyacencia[vertice][vecino] = 1
                    matriz_adyacencia[vecino][vertice] = 1

        return subarbol

    # Si el grafo es conexo, generamos el árbol generador
    if es_conexa(grafica):
        bfs(0)  # Realizamos un BFS desde el nodo 0 para obtener el árbol generador
        return matriz_adyacencia  # Retornamos la matriz de adyacencia del árbol generador
    else:
        # Si el grafo no es conexo, generamos el bosque generador
        for vertice in range(n):
            if not visitado[vertice]:  # Si el nodo no ha sido visitado
                bfs(vertice)  # Llamamos a BFS desde ese nodo para generar el árbol del componente conexo
        
        return matriz_adyacencia  # Retornamos la matriz de adyacencia del bosque generador

grafica1 = [
    [0, 1, 0, 0],  
    [1, 0, 0, 0],  
    [0, 0, 0, 1],  
    [0, 0, 1, 0]  
]

print(arbol_generador(grafica1))

# Ejemplo de grafo no conexo
grafica2 = [
    [0, 1, 0, 0, 0],  
    [1, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]  
]

print(arbol_generador(grafica2))