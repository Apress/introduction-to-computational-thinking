class Node(object):
    def __init__(self, value,
                 left = None,
                 right = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({}, left = {}, right = {})'.format(
            repr(self.value),
            repr(self.left),
            repr(self.right)
        )

# Persistent implementation
def contains(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    if node.value > value:
        return contains(node.left, value)
    if node.value < value:
        return contains(node.right, value)

def insert(node, value):
    if node is None:
        return Node(value)
    if node.value == value:
        return node
    elif node.value > value:
        return Node(node.value,
                    left = insert(node.left, value),
                    right = node.right)
    elif node.value < value:
        return Node(node.value,
                    left = node.left,
                    right = insert(node.right, value))

def remove(node, value):
    if node is None:
        return None
    if node.value > value:
        return Node(node.value,
                    left = remove(node.left, value),
                    right = node.right)
    if node.value < value:
        return Node(node.value,
                    left = node.left,
                    right = remove(node.right, value))

    # we have value == node.value
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left

    replacement = rightmost_value(node.left)
    return Node(replacement,
                remove(node.left, replacement),
                node.right)

def rightmost_value(node):
    if node.right is None:
        return node.value
    else:
        return rightmost_value(node.right)

def tree_iter(node):
    if node is None: return # Done iterating
    yield from tree_iter(node.left)
    yield node.value
    yield from tree_iter(node.right)

class SearchTreeSet(object):
    def __init__(self, seq = ()):
        self.tree = None
        for value in seq:
            self.add(value)

    def add(self, element):
        self.tree = insert(self.tree, element)

    def remove(self, element):
        if element not in self:
            raise KeyError()
        self.tree = remove(self.tree, element)

    def __iter__(self):
        return tree_iter(self.tree)

    def __contains__(self, element):
        return contains(self.tree, element)

    def __repr__(self):
        return 'SearchTreeSet(tree_iter(' + repr(self.tree) + '))'

x = SearchTreeSet([1,2,1,4])
print(x)
for i in range(5):
    print(f"is {i} in {list(x)}? {i in x}")
print()

# Ephemeral implementation
class Node(object):
    def __init__(self, value,
                 parent = None,
                 left = None,
                 right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

        # guaranteeing consistencey
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def __repr__(self):
        return 'Node({}, left = {}, right = {})'.format(
            repr(self.value),
            repr(self.left),
            repr(self.right)
        )

def find_node(node, value):
    p, n = None, node
    while n:
        if n.value == value:
            return n
        elif n.value > value:
            # go left
            p, n = n, n.left
        elif n.value < value:
            # go right
            p, n = n, n.right
    return p

def contains(node, value):
    return find_node(node, value).value == value

def insert(node, value):
    n = find_node(node, value)
    if n.value == value:
        return # already here
    elif n.value > value:
        n.left = Node(value, parent = n)
    else:
        n.right = Node(value, parent = n)

def get_rightmost(node):
    while node.right is not None:
        node = node.right
    return node

def replace(child, new_child):
    if child.parent.left == child:
        child.parent.left = new_child
    else:
        child.parent.right = new_child
    if new_child is not None:
        new_child.parent = child.parent

def remove(node, value):
    n = find_node(node, value)
    if n.value != value:
        raise KeyError()

    if n.left is None:
        replace(n, n.right)
    elif n.right is None:
        replace(n, n.left)
    else:
        rightmost = get_rightmost(n.left)
        n.value = rightmost.value
        remove(n.left, rightmost.value)

class SearchTreeSet(object):
    def __init__(self, seq = ()):
        self.tree = Node(None) # dummy node
        for value in seq:
            self.add(value)

    def add(self, element):
        if self.tree.left is None:
            self.tree.left = Node(element, parent = self.tree)
        else:
            insert(self.tree.left, element)

    def remove(self, element):
        if self.tree.left is None:
            raise KeyError()
        remove(self.tree.left, element)

    def __iter__(self):
        return tree_iter(self.tree.left)

    def __contains__(self, element):
        if self.tree.left is None:
            return False
        return contains(self.tree.left, element)

    def __repr__(self):
        return 'SearchTreeSet(tree_iter(' + repr(self.tree.left) + '))'


x = SearchTreeSet([1,2,1,4])
print(x)
for i in range(5):
    print(f"is {i} in {list(x)}? {i in x}")
x.remove(2)
print(x)
for i in range(5):
    print(f"is {i} in {list(x)}? {i in x}")
print()
