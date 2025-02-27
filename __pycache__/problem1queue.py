class Queue:
    def __init__(self):
        self.list1=[]
        self.size=0
    
    def enqueue(self,value):
        self.list1.append(value)
        self.size+=1
    
    def dequeue(self):
        if self.size==0:
            return None
        else:
            self.size-=1
            currentval=self.list1[0]
            self.list1=self.list1[1:]
            return currentval
    
    def getFront(self):
        if self.size==0:
            return None
        else:
            return self.list1[0]
    
    def Display(self):
        for i in range(self.size):
            print(self.list1[i])
    
queue1 = Queue()

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
##queue1.Display()
##print(queue1.getFront())
queue1.dequeue()
queue1.dequeue()
queue1.Display()
