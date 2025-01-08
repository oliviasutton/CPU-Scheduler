This program simulates a CPU scheduler using a variety of data structures, such as queues and stacks, to manage processes and their corresponding functions.

Key Components:
CPU_Scheduler: Handles the queue of processes. It supports adding processes to the queue, moving processes to the back, removing processes from the queue, and peeking at the process at the front.

Executive: Reads commands from a file and processes them. It can start processes, call functions on processes, handle returns, and raise exceptions. It interacts with the CPU_Scheduler to manage processes.

Process: Represents a process in the system. It has a stack to manage the functions associated with the process. Each process starts with a main function and can push or pop functions from its stack.

Function: Represents a function that a process can call. It can have an associated exception flag.

LinkedQueue: Implements a queue to manage processes in the CPU scheduler. It supports standard operations like enqueue, dequeue, peek, and checking if the queue is empty.

Stack: Implements a stack to manage function calls within each process. Functions are pushed onto or popped from the stack as processes call or return from functions.

Workflow:
The program reads commands from a file (e.g., "test2.txt").
Commands include starting processes, calling functions, returning from functions, or raising exceptions.
Each command is processed, and the appropriate actions (like adding processes to the queue or handling exceptions) are taken.
