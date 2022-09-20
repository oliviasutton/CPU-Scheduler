



from stack import Stack
from node import Node 
from linkedqueue import LinkedQueue
from process import Process
from function import Function
from cpu import CPU_Scheduler
class Executive:
    def __init__(self, file_name:  str):
        #open the file and read line by line
        with open(file_name, 'r') as f: self.lines = f.readlines()

    

    def run(self):
       
        cpu = CPU_Scheduler()
        # Iterate through line
        # For each line:
        #   split by spaces (keywords = line.split())
        #   first item will be the command (e.g, START, CALL, RETURN, RAISE)
        #   if the command is START, the second item will be the process name
        #   if the command is CALL, the second item will be the function name, and
        #   the third item will be the exception boolean
        # ["START", "itunes\n"]
        # ["START", "itunes"]
        for line in self.lines:
            element = line.split()
            if element[0] == "START":
                p = Process(element[1])
                cpu.add(p)
                print(f"{p.name} added to queue")
            elif element[0] == "CALL":
                excep = True if element[2] == 'yes' else False 
                f = Function(element[1], excep)
                cpu.back(f)
                print(f"{p.name} calls {f.name}")
            elif element[0] == "RETURN":
                #if the process has a function to it, dequeue and then enqueue it
                p = cpu.remove()
                f = p.remove()
                print(f"{p.name} returns from {f.name}")
                if not p.is_empty():
                     cpu.add(p)
                else:
                    print(f"{p.name} process has ended")
            elif element[0] == "RAISE":
                p = cpu.peek()
                if p.exception():
                    cpu.remove()
                    print ("Process ended")
                else: 
                    print (f"{p.name} has exception handled by: {f.name}")
                
    
            
                



