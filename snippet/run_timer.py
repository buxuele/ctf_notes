import time
import random


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


timer = ExecutionTime()

"""
run some code here:

sample_list = list()
my_list = [random.randint(1, 888898) for n in
           range(1, 1000000) if n % 2 == 0]
print("something about the list")

"""

print("finished in {} seconds.".format(timer.duration()))
