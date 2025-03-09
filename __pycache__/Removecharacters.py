#Given two strings string1 and string2, remove those characters from the first string(string1) which are present in the second string(string2). Both strings are different and contain only lowercase characters.
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


def RemoveChar(w,s):
    stack=Stack()
    set1=set(s)
    t=""
    for i in range(len(w)-1,-1,-1):
        stack.push(w[i])
    while stack.size>0:
        key=stack.pop()
        if key not in set1:
            t+=key
    return t
print(RemoveChar("“occurrence”","car"))

