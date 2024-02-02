import random
import time
from collections import deque
# Using a doubly ended queue to implement the PCB

class ProgramControl:
    # This is the main control block
    def __init__(self,PID,complete_time):
        self.PID = PID
        self.complete_time = complete_time
        self.time_left = complete_time

class LongTerm:
    # THis is the class fro long term scheduling
    def __init__(self):
        self.processes = deque()

    def new_process(self,PID,complete_time):
        # Function to add a new process to long term scheduling
        p = ProgramControl(PID,complete_time)
        self.processes.append(p)
        print(f'process {PID} added to long term\n')

    def delete_process(self):
        # Function to remove a process after long term scheduling is completed
        p = self.processes.popleft()
        print(f'process {p.PID} removed from long term\n')
        return p

class ShortTerm:
    def __init__(self):
        self.running_process = None
    
    def new_process(self,p):
        # Function to add a new process to short term scheduling
        self.running_process = p
        print(f'process {self.running_process.PID} added to short term\n')

    def delete_process(self):
        # Function to remove a process after short term scheduling is completed
        print(f'process {self.running_process.PID} removed from short term\n')
        self.running_process = None
        

    def run(self):
        if self.running_process:
            time.sleep(1)
            self.running_process.time_left -= 1
            if self.running_process.time_left == 0:
                self.delete_process()

def program(long_term, short_term,number,time_range):
    # This is the main function to simulate the running process of the PCB
    for i in range(number):
        complete_time = random.randint(*time_range)
        long_term.new_process(i, complete_time)
    
    while long_term.processes:
        p = long_term.delete_process()
        short_term.new_process(p)

        while short_term.running_process:
            short_term.run()

        time.sleep(1)

    print("***Execution over***")

def main():
    lt = LongTerm()
    st = ShortTerm()

    program(lt,st,5,(1,5))

if __name__ == "__main__":
    main()