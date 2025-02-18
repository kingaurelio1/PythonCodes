class Nodo:
    def __init__(self, valor):
        self.valor = valor  # El dato que contiene el nodo
        self.siguiente = None  # Enlace al siguiente nodo (inicialmente es None)


class LinkedList:
    def __init__(self):
        self.cabeza = None  # La cabeza de la lista (inicialmente está vacía)

    # Método para agregar un nodo al final de la lista
    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)  # Creamos un nuevo nodo con el valor dado
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo será la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si no está vacía, recorreremos la lista hasta llegar al último nodo
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            # Ahora el nodo_actual es el último nodo, entonces su "siguiente" será el nuevo nodo
            nodo_actual.siguiente = nuevo_nodo

    # Método para recorrer la lista e imprimir los valores
    def recorrer(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("null")  # Esto indica el final de la lista

    # Método para eliminar un nodo por valor
    def eliminar(self, valor):
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        # Si la cabeza es el nodo que queremos eliminar
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return

        # Buscar el nodo a eliminar
        nodo_actual = self.cabeza
        while nodo_actual.siguiente and nodo_actual.siguiente.valor != valor:
            nodo_actual = nodo_actual.siguiente
        
        # Si encontramos el nodo, lo eliminamos
        if nodo_actual.siguiente:
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente
        else:
            print(f"El valor {valor} no se encontró en la lista.")
    def invertir(self):
        prev = None
        current = self.cabeza
        while current:
            next_node = current.siguiente  # Guardamos el siguiente nodo
            current.siguiente = prev  # Invertimos el puntero del nodo actual
            prev = current  # Movemos prev a current
            current = next_node  # Movemos current al siguiente nodo
        
        self.cabeza = prev  # Al final, prev será el nuevo primer nodo
# create a new linked list

# Ejemplo de uso:
mi_lista = LinkedList()
mi_lista.agregar_al_final(10)
mi_lista.agregar_al_final(20)
mi_lista.agregar_al_final(30)

print(mi_lista)
