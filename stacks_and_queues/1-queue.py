"""
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
"""

class Queue:

    def __init__(self):
        self.storage = []

    def add(self, val):
        self.storage.append(val)

    def remove(self):
        # Slow because all of the other elements have to be shifted by one.
        self.storage.pop(0)

    def peak(self):
        return None if self.is_empty() else self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

    def __str__(self):
        return str(self.storage)

q = Queue()

q.add('1')
q.add('2')
q.add('3')

print(q.peak())

print(q)
q.remove()
print(q)
q.remove()
print(q)
q.remove()
print(q)
