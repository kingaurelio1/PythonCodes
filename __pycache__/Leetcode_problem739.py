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

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

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
def dailyTemperatures(a):
    t=Stack()
    pointer=len(a)-1
    sum1=1
    while pointer>-1:
        print(t)
        if t.size==0:
            t.push([a[pointer],pointer])
            a[pointer]=0
            pointer-=1
            sum1=1
        else:
            if a[pointer] < t.peek()[0]:
                k=[a[pointer],pointer]
                a[pointer]=t.peek()[1] - pointer
                t.push(k)
                pointer-=1
                sum1=1
            else:
                t.pop()
                sum1+=1
                print(t,a[pointer])
    return a
print(dailyTemperatures([73,74,75,71,69,72,76,73]))