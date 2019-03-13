class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self.data
        if self.right:
            for node in self.right:
                yield node

    def __getitem__(self, key):
        node = self.get(key)
        if node:
            return node
        raise KeyError(key)

    def get(self, data):
        if data < self.data:
            return self.left.get(data) if self.left else None
        elif data > self.data:
            return self.right.get(data) if self.right else None
        return self

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.left.parent = self
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                self.right.parent = self
            else:
                self.right.insert(data)

    def is_left_child(self):
        return self.parent and self is self.parent.left

    def is_right_child(self):
        return self.parent and self is self.parent.right

    def count_children(self):
        return bool(self.left) + bool(self.right)

    def max(self):
        node = self
        while node.right:
            node = node.right
        return node

    def min(self):
        node = self
        while node.left:
            node = node.left
        return node

    def get_successor(self):
        if self.right:
            return self.right.min()
        node = self
        while node.is_right_child():
            node = node.parent
        return node.parent

    def get_predecessor(self):
        if self.left:
            return self.left.max()
        node = self
        while node.is_left_child():
            node = node.parent
        return node.parent

    def delete(self, data):

        node = self.get(data)

        if not node:
            return

        children_count = node.count_children()

        if children_count == 0:
            # Node has no children: remove it.
            # Fix references.
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
            del node

        elif children_count == 1:
            # Node has 1 child: replace it by its child.
            child = node.left or node.right
            if node.is_left_child():
                # Remove `node` from the tree by fixing references.
                node.parent.left = child
                child.parent = node.parent
                del node
            elif node.is_right_child():
                # Remove `node` from the tree by fixing references.
                node.parent.right = child
                child.parent = node.parent
                del node
            else:
                # If there is no parent, we are at the root.
                root = node
                root.data = child.data
                # Remove `child` from the tree by fixing references.
                root.left = child.left
                root.right = child.right
                if child.left:
                    child.left.parent = root
                if child.right:
                    child.right.parent = root
                del child

        else:
            # Node has 2 children: replace it by its successor.
            # Because the node has 2 children, its successor is guaranteed to
            # be somewhere on its right side. If the successor has children,
            # they can only be on the right side.
            succ = node.get_successor()
            node.data = succ.data
            # Remove `succ` from the tree by fixing references.
            if succ.is_left_child():
                succ.parent.left = succ.right
            else:
                succ.parent.right = succ.right
            if succ.right:
                succ.right.parent = succ.parent
            del succ

    def pprint(self, level=0):
        if self.right:
            self.right.pprint(level + 1)
        print(f"{' ' * 4 * level}{self.data}")
        if self.left:
            self.left.pprint(level + 1)

    def get_height(self):
        return 1 + max(
            self.left.get_height() if self.left else -1,
            self.right.get_height() if self.right else -1
        )

    def _check_balance(self):
        left = self.left._check_balance() if self.left else -1
        right = self.right._check_balance() if self.right else -1
        if abs(left - right) > 1:
            raise ValueError('Unbalanced tree.')
        return max(left, right) + 1

    def is_balanced(self):
        try:
            self._check_balance()
            return True
        except ValueError:
            return False

    def is_valid(self):
        prev = None
        for data in self:
            if prev and prev > data:
                return False
            prev = data
        return True

bst = Node(12)
bst.insert(6)
bst.insert(14)
bst.insert(3)
bst.insert(8)
bst.insert(20)
bst.insert(5)
bst.insert(1)
bst.insert(150)
bst.insert(99)
bst.insert(7)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(13)

bst.pprint()

print(bst.is_valid())
