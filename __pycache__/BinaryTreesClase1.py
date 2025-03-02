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
            maxNode=self.root
            while maxNode:
                if maxNode.right is not None:
                    maxNode=maxNode.right
                else:
                    break                
            return maxNode.value
    def secondlargest(self):
        if self.root is None or (self.root.left is None and self.root.right is None):
            return None  # No hay suficiente nodos para tener un segundo más grande
    
        maxNode = self.root
        parent = None
    
        while maxNode.right is not None:
            parent = maxNode
            maxNode = maxNode.right
    
    # Si el máximo tiene un subárbol izquierdo
        if maxNode.left is not None:
            maxNode = maxNode.left
            while maxNode.right is not None:
                maxNode = maxNode.right
            return maxNode.value
    
    # Si no tiene subárbol izquierdo, el padre es el segundo más grande
        return parent.value
    
    def search(self,value):
        if self.root is None:
            return False
        else:
            searchNode=self.root
            t=False
            while searchNode:
                if searchNode is not None and searchNode.value < value:
                    searchNode=searchNode.right
                elif searchNode is not None and searchNode.value > value:
                    searchNode=searchNode.left
                else:
                    t=True
                    break
            return t
    
    def reverseTree(self,nodo):
        if nodo is None:
            return self.root
        else:
            nodo.left, nodo.right=nodo.right, nodo.left
            self.reverseTree(nodo.left)  # Recursión en el hijo izquierdo
            self.reverseTree(nodo.right) 
            return nodo
    def reverseFullTree(self):
        self.reverseTree(self.root)
    def imprimirArbol(self,node,nivel=0):
        nivel=0
        if node is not None:
            # Primero imprimir los hijos derechos (si los hay)
            self.imprimirArbol(node.right, nivel + 1)
            
            # Luego imprimir el nodo actual con una indentación basada en su nivel
            print(' ' * 4 * nivel + '->', node.value)
            
            # Finalmente imprimir los hijos izquierdos
            self.imprimirArbol(node.left, nivel + 1)
    def imprimirInorden(self, nodo):
        if nodo is None:
            return
        self.imprimirInorden(nodo.left)  # Recursión sobre el hijo izquierdo
        print(nodo.value, end=' ')  # Imprimir el valor del nodo
        self.imprimirInorden(nodo.right)  # Recursión sobre el hijo derecho
    
    def imprimir(self):
        self.imprimirInorden(self.root)

    def depth(self,node):
        pass
    

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(17)
print(bst.imprimir())
##print(bst.lookup(7))  
#print(bst.imprimirArbol(Node(10)))
print(bst.min())  
print(bst.largest())
print(bst.search(8))
print(bst.reverseFullTree())
print(bst.imprimir())