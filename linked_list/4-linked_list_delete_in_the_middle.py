"""
Implement an algorithm to delete a node in the middle (ie., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.

Input: the node c from the linked list a -> b -> c -> d -> e -> f

Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""

class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return str(self.cargo)

def print_forward(node):
    while node:
        print(node.cargo)
        node = node.next

def delete(node):
    """
    Simply copy the data from the next node over to the current node.
    """
    if not node or not node.next:
        return False
    node.cargo = node.next.cargo
    node.next = node.next.next
    return True

f = Node('f')
e = Node('e', _next=f)
d = Node('d', _next=e)
c = Node('c', _next=d)
b = Node('b', _next=c)
a = Node('a', _next=b)

print('-' * 40)
print_forward(a)

print('-' * 40)
delete(c)
print_forward(a)
