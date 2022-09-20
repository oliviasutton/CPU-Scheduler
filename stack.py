from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def push(self, value):
        #push value onto stack
        entry = Node(value)
        if self.is_empty():
            self._top = entry
        else:
            temp = self._top
            self._top = entry
            self._top.next = temp 
        
    def pop(self):
        #take away from stack
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        else:
            temp = self._top
            self._top = self._top.next
            return temp.value

    def is_empty(self):
        #check if stack is empty
        return self._top == None

    def peek(self):
        #peek to see the top of the stack
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        else:
            return self._top