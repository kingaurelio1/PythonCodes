class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        

class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    
    def peek(self):
        return self.s1.peek()
    
    def push(self,value):
        self.s1.push(value)
    
    def is_empty(self):
        if self.s1.length==0:
            return True
        else:
            return False
    
    def pop(self):
        if self.s1.length==0:
            return None
        elif self.s1.top==self.s1.bottom:
            self.s1.pop()
        else:
            while self.s1.length > 0:
                t=self.s1.pop()
                self.s2.push(t)
            self.s2.pop()

n=Queue()
n.push(3)
n.push(4)
n.push(5)
print(n.pop())
