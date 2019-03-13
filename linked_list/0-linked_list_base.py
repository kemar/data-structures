class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, cargo):
        _next = self.head
        self.head = Node(cargo, _next)
        self.length += 1


class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return str(self.cargo)


linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print('-' * 40)
print(linked_list.length)
