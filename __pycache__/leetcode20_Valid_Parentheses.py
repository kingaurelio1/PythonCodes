#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
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


def validParentheses(s):
    if len(s)%2==1:
        return False
    else:
        stack=Stack()
        i=0
        while i<len(s):
            if s[i] in "({[":
                stack.push(s[i])
                i+=1
            elif s[i] in ")]}" and stack.size==0:
                return False
            elif s[i] ==")" and stack.peek()=="(":
                stack.pop()
                i+=1
            elif s[i] =="]" and stack.peek()=="[":
                stack.pop()
                i+=1
            elif s[i] =="}" and stack.peek()=="{":
                stack.pop()
                i+=1
            else:
                return False
    return True
print(validParentheses("[(])"))
