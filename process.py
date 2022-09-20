from stack import Stack
from function import Function

# Process:
# has a stack
# pushes and pops Function objects
# function objects come from input file, will be sent from Exeec\\cutive


class Process:

    def __init__(self, name: str):
        self.name = name
        self.stack = Stack()
        self.add(Function("main", exception=False), do_print=False)

    def add(self, function: Function, do_print = True):
        #push a function onto the stack
        self.stack.push(function)

    def remove(self):
        #remove from the stack
        return self.stack.pop()

    def is_empty(self) -> bool:
        #check if stack is empty
        return self.stack.is_empty()

    def exception(self):
        #if the stack is not empty and it cannot handle an exception, pop the function and then
        #return if the stack is empty or
        #self.stack.pop()
        print(f"{self.name} encountered a raised exception by: {self.stack.peek().value.name}")
        while self.stack.is_empty() is False and self.stack.peek().value.exception != True:
            print(f"{self.name} ends {self.stack.peek().value.name} due to unhandled exception")
            self.stack.pop()
        
        h = self.stack.is_empty()
        return h 
          

