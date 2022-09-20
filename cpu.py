from linkedqueue import LinkedQueue


class CPU_Scheduler:

#going to have enqueue and dequeue

    def __init__(self):
        self.queue = LinkedQueue()
        
    
    def add(self, p):
        #add a process to the queue
        self.queue.enqueue(p)

    def back(self, func):
        #send a process to the back of the queue
        p = self.queue.dequeue()
        p.add(func)
        self.queue.enqueue(p)

    def remove(self):
        #remove a process from the queue
        p = self.queue.dequeue()
        return p

    def peek(self):
        #look at the front of the queue
        p = self.queue.peek_front()
        return p 