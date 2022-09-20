
from node import Node

class LinkedQueue:

    def __init__(self):
        self._front = None
        self._back = None 

    def enqueue(self, value):
        # add a new node to the queue at the back
        new = Node(value)
        if self.is_empty():
            self._front = new
            self._back = new
        else:
            self._back.next = new
            self._back = new

    
    def dequeue(self):
        #take from out of the front of the queue
        temp = self.peek_front()
        self._front = self._front.next
        return temp

    def is_empty(self):
        #check if empty
        return self._front == None


    def peek_front(self):
        #check the front of the queue
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        else:
            return self._front.value

    