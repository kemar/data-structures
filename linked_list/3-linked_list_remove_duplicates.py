"""
Write code to remove duplicates from an unsorted linked list.
"""

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, cargo):
        _next = self.head
        self.head = Node(cargo, _next)
        self.length += 1

    def remove_duplicates(self):
        seen = set()
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.cargo in seen:
                prev_node.next = curr_node.next
                self.length -= 1
            else:
                seen.add(curr_node.cargo)
                prev_node = curr_node
            curr_node = curr_node.next

    def remove_duplicates_with_runner(self):
        """
        Same as above method without additional data structure.

        Iterate with 2 pointers: `curr_node` which iterates through the linked list,
        and `runner_node` which checks all subsequent nodes for duplicates.

        O(1) space, O(n^2) time
        """
        curr_node = self.head
        while curr_node:
            runner_node = curr_node
            while runner_node.next:
                if runner_node.next and runner_node.next.cargo == curr_node.cargo:
                    runner_node.next = runner_node.next.next
                else:
                    runner_node = runner_node.next
            curr_node = curr_node.next

    def print_list(self):
        node = self.head
        values = []
        while node:
            values.append(node.cargo)
            node = node.next
        print(f"{values}")


class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def print_forward(self):
        print(self),
        if self.next:
            self.next.print_forward()

    def __str__(self):
        return str(self.cargo)


linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(4)
linked_list.add(4)

print('-' * 40)
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_list()

print('-' * 40)
linked_list.remove_duplicates()
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_list()


linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(4)
linked_list.add(4)

print('-' * 40)
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_list()

print('-' * 40)
linked_list.remove_duplicates_with_runner()
print(f'Head = {linked_list.head.cargo}')
print(f'Length = {linked_list.length}')
linked_list.print_list()
