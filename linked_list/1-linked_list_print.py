"""
Write code to print a linked list forward and backward.
"""

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, cargo):
        _next = self.head
        self.head = Node(cargo, _next)
        self.length += 1

    def print_forward(self):
        print('[', end='')
        if self.head:
            self.head.print_forward()
        print(']')

    def print_backward(self):
        print('[', end='')
        if self.head:
            self.head.print_backward()
        print(']')


class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def print_forward(self):
        print(self, end=',' if self.next else '')
        if self.next:
            self.next.print_forward()

    def print_backward(self):
        if self.next:
            self.next.print_backward()
        print(self.cargo, end=',')

    def __str__(self):
        return str(self.cargo)


linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print('-' * 40)
linked_list.print_forward()

print('-' * 40)
linked_list.print_backward()
