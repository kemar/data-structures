class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node, end=' ')


tree = Node('+', left=Node(1), right=Node('*', left=Node(2), right=Node(3)))

in_order_traversal(tree)
