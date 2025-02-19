from limkedlists2 import Node 
from limkedlists2 import LinkedList

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        return self.top
    
    def push(self,value):
        N=Node(value)
        
        if self.length==0:
            self.top = N
            self.bottom = N
        else:
            newpointer=self.top
            self.top = N
            self.top.next = newpointer
        
        self.length+=1


    def pop(self):
        if self.length==0:
            return None
        elif self.top==self.bottom:
            self.bottom=None
        else:
            newpointer=self.top
            self.top=self.top.next
            self.length-=1
            return self
        