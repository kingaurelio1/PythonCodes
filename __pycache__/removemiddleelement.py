#Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0


    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            return None

        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next # Make the new node point to the current head
        self.head.next = node #!!! # Update the head to be the new node
        self.size += 1


    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next #!!! changed
        self.size -= 1
        return remove.value
#Primera solución usando stacks.
def removeMiddle(a):
    stack=Stack()
    l=[]
    middle=(len(a)-1)//2
    for i in range(len(a)-1,-1,-1):
        if i!=middle:
            stack.push(a[i])
    while stack.size>0:
        l.append(stack.pop())
    return l
print(removeMiddle([1,2,3,4,5,6]))

#Usando los dos punteros.

def RemovingMiddle(a):
    l=0
    r=1
    middle=(len(a)-1)//2
    while r<len(a):
        if middle<=l:
            a[l],a[r]=a[r],a[l]
            l+=1
            r+=1
        else:
            l+=1
            r+=1
    a.pop()
    return a 
print(RemovingMiddle([1,2,3,4,5,6]))