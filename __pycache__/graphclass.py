#Se define la clase de las gráficas

class Graph:
    def __init__(self):
        self.numberofnodes=0
        self.adjacentlist={}

    def addNode(self,node):
        self.adjacentlist[node]=[]
        self.numberofnodes+=1
    
    def addEdge(self,node1,node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
        