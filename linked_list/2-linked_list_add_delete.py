"""
Write code to add, search and remove items from an unsorted linked list.
"""

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, cargo):
        _next = self.head
        self.head = Node(cargo, _next)
        self.length += 1

    def search(self, value):
        node = self.head
        while node:
            if node.cargo == value:
                return node
            node = node.next
        return None

    def delete(self, k):
        node = self.head

        # The node to delete is the head, change it.
        if node.cargo == k:
            self.head = node.next
            del node
            self.length -= 1
            return

        # The node to delete is not the head, update the chain.
        while node.next:
            if node.next.cargo == k:
                node.next = node.next.next
                del node.next
                self.length -= 1
                return
            node = node.next

    def print_forward(self):
        print('[', end='')
        if self.head:
            self.head.print_forward()
        print(']')


class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def print_forward(self):
        print(self, end=',' if self.next else '')
        if self.next:
            self.next.print_forward()

    def __str__(self):
        return str(self.cargo)


linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print('-' * 40)
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_forward()

print('-' * 40)
linked_list.delete(3)
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_forward()
