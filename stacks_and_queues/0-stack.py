"""
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
"""

class Stack:

    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        self.storage.pop(-1)

    def peak(self):
        return None if self.is_empty() else self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

    def __str__(self):
        return str(self.storage)

s = Stack()

print(s.peak())

s.push('1')
s.push('2')
s.push('3')

print(s)

print(s.peak())

s.pop()

print(s)
