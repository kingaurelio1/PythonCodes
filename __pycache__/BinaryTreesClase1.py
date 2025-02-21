#Binary trees
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node  
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:  
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    if current_node.right is None:  
                        current_node.right = new_node
                        return self
                    current_node = current_node.right
    def lookup(self,value):
        if self.root is None:
            return False
        else:
            current_node = self.root
            while current_node:
                if value < current_node.value:
                    current_node=current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
                elif value==current_node.value:
                    return current_node
            return False
    def remove(self, value):
        if self.root is None:
            return False  # El árbol está vacío, no hay nada que eliminar
    
        # Función auxiliar para eliminar el nodo
        def remove_node(node, value):
            if node is None:
                return node  # Si el nodo es None, no hacer nada

        # Buscar el nodo a eliminar
            if value < node.value:
                node.left = remove_node(node.left, value)  # Buscar en el subárbol izquierdo
            elif value > node.value:
                node.right = remove_node(node.right, value)  # Buscar en el subárbol derecho
            else:
            # Si encontramos el nodo a eliminar:
            
                # Caso 1: El nodo no tiene hijos (es una hoja)
                if node.left is None and node.right is None:
                    return None  # Simplemente eliminamos el nodo

            # Caso 2: El nodo tiene un solo hijo
                if node.left is None:
                    return node.right  # El nodo derecho reemplaza al nodo eliminado
                elif node.right is None:
                    return node.left  # El nodo izquierdo reemplaza al nodo eliminado

            # Caso 3: El nodo tiene dos hijos
            # Encontramos el sucesor (el valor mínimo en el subárbol derecho)
                successor = self._get_min(node.right)
                node.value = successor.value  # Reemplazamos el valor del nodo con el sucesor
                node.right = remove_node(node.right, successor.value)  # Eliminamos el sucesor

            return node  # Retornamos el nodo actualizado

    # Llamamos a la función auxiliar con la raíz del árbol
        self.root = remove_node(self.root, value)
        return True  # Si llegamos aquí, la eliminación fue exitosa

    def min(self):
        if self.root is None:
            return None
        else:
            minNode=self.root
            while minNode:
                if minNode.left is not None:
                    minNode=minNode.left
                    break                
            return minNode.value
    def count(self,n,m):
        self.sum=0
        if self.root is None:
            return self.sum
        else:
            currentNode = self.root
            while currentNode:
                return None
    
    def largest(self):
        if self.root is None:
            return None
        else:
            r=self.min()
            maxNode=self.root
            while maxNode:
                if maxNode.right is not None:
                    maxNode=maxNode.right
                    break                
            return maxNode.value
         

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

##print(bst.lookup(7))  

print(bst.min())  
print(bst.largest())