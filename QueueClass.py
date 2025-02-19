from limkedlists2 import Node

class Queue:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0
    
    def peek(self):
        if self.length==0:
            return None
        else:
            return self.top
    
    def enqueue(self,value):
        N=Node(value)
        if self.length==0:
            self.top=N
            self.bottom=N
        else:
            pointer=self.bottom
            self.bottom=N
            self.bottom.next=pointer
        self.length+=1

    def dequeue(self):
        if self.length==0:
            return None
        elif self.top==self.bottom:
            self.top=None
        else:
            pointer =self.top
            self.top=self.top.next
            self.length-=1
            return self