#Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array. 
#Note: The Next Greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 
#primera idea

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
def NGE(a):
    l=0
    r=1
    while l<len(a):
        print(a,l,r)
        if l==len(a)-1:
            a[l]=-1
            break
        elif r==len(a)-1 and a[l] >= a[r]:
            a[l]=-1
            l+=1
            r=l+1
        elif r==len(a)-1 and a[l] < a[r]:
            a[l]=a[r]
            l+=1
            r=l+1
        elif a[l]<a[r]:
            a[l]=a[r]
            l+=1
            r=l+1
        elif a[l]>=a[r]:
            r+=1
    return a
#print(NGE( [6, 8, 0, 1, 3]))
#No funciona

#Segunda idea:
def NGE2(a):
    t=Stack()
    for i in range(len(a)):
        t.push(a[i])
    pointer=len(a)-1
    while pointer >-1:
        print(a,t.size,t.peek(),pointer,a[pointer])
        if a[pointer] < t.peek():
            a[pointer]=t.peek()
            t.pop()
            pointer-=1
        else:
            if t.size-2 <= pointer:
                a[pointer]=-1
            else:
                t.pop()
            pointer-=1
    return a
#print(NGE2( [1,4,3,6]))


#Tercera idea:
def NGE3(a):
    t=Stack()
    pointer=len(a)-1
    while pointer>-1:
        if t.size==0:
            t.push(a[pointer])
            a[pointer]=-1
            pointer-=1
        else:
            if a[pointer] < t.peek():
                k=a[pointer]
                a[pointer]=t.peek()
                t.push(k)
                pointer-=1
            else:
                t.pop()
    return a
print(NGE3([5,4,3,2,1]))