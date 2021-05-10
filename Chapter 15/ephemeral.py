import weakref
class WeakRefProperty(object):
    def __get__(self, obj, cls):
        value = obj.__dict__[id(self)]
        if type(value) is weakref.ref:
            return value()
        else:
            return value

    def __set__(self, obj, value):
        try:
            value = weakref.ref(value)
        except TypeError:
            # can't make a weak ref
            pass
        obj.__dict__[id(self)] = value
        

RED = 0
BLACK = 1


class Node(object):
    parent = WeakRefProperty()

    # Always update parent when left or right is set
    def get_left(self):
        return self._left
    def set_left(self, left):
        self._left = left
        left.parent = self
    left = property(get_left, set_left)

    def get_right(self):
        return self._right
    def set_right(self, right):
        self._right = right
        right.parent = self
    right = property(get_right, set_right)

    @property
    def is_red(self):
        return self.colour is RED
    @property
    def is_black(self):
        return self.colour is BLACK

    @property
    def is_left(self):
        return self is self.parent.left
    @property
    def is_right(self):
        return not self.is_left

    @property
    def sibling(self):
        p = self.parent
        if p.left is self:
            return p.right
        else:
            return p.left
    @property
    def uncle(self):
        return self.parent.sibling
    @property
    def grandparent(self):
        return self.parent.parent

    @property
    def is_inner(self):
        return self.is_left and self.parent.is_right or\
               self.is_right and self.parent.is_left
    @property
    def is_outer(self):
        return not self.is_inner

    @property
    def inner_child(self):
        if self.is_left:
            return self.right
        else:
            return self.left

    @property
    def outer_child(self):
        if self.is_left:
            return self.left
        else:
            return self.right

    def replace_child(self, current, new):
        if current == self.left:
            self.left = new
        else:
            self.right = new

    def rotate_left(self):
        self.parent.replace_child(self, self.right)
        b = self.right.left
        self.right.left = self
        self.right = b

    def rotate_right(self):
        self.parent.replace_child(self, self.left)
        b = self.left.right
        self.left.right = self
        self.left = b

    def rotate(self):
        if self.is_left:
            self.parent.rotate_right()
        else:
            self.parent.rotate_left()

class EmptyTree(Node):
    def __init__(self):
        self.colour = BLACK
EMPTY_TREE = EmptyTree()

class Tree(Node):
    def __init__(self, value,
                 colour = RED,
                 left = EMPTY_TREE,
                 right = EMPTY_TREE):
        self.value = value
        self.colour = colour
        self.parent = None
        self.left = left
        self.right = right

# Don't call with a None node
def find_node(tree, value):
    n = tree
    while True:
        if n.value == value:
            return n
        elif n.value > value:
            # go left
            if n.left is EMPTY_TREE:
                return n
            n = n.left
        else: # n.value < value:
            # go right
            if n.right is EMPTY_TREE:
                return n
            n = n.right

def contains(tree, value):
    return find_node(tree, value).value == value

def insert(tree, value):
    n = find_node(tree, value)
    if n.value == value:
        return # already here

    new_node = Tree(value)
    if n.value > value:
        n.left = new_node
    else:
        n.right = new_node
    fix_red_red(new_node)

def fix_red_red(node):
    while node.parent.is_red:
        if node.uncle.is_red:
            # Case 1
            node.parent.colour = BLACK
            node.uncle.colour = BLACK
            node.grandparent.colour = RED
            node = node.grandparent
        elif node.is_inner:
            # Case 2
            old_parent = node.parent
            node.rotate()
            node = old_parent
        else:
            # Case 3
            node.parent.rotate()
            node.parent.colour = BLACK
            node.sibling.colour = RED
            return # Done with fixing

def get_rightmost(node):
    while node.right is not EMPTY_TREE:
        node = node.right
    return node

def remove(tree, value):
    n = find_node(tree, value)
    if n.value != value:
        return # value wasn't in the tree

    if n.left is not EMPTY_TREE and n.right is not EMPTY_TREE:
        rightmost = get_rightmost(n.left)
        n.value = rightmost.value
        remove(n.left, rightmost.value)

    else:
        replacement = n.left \
                      if n.right is EMPTY_TREE \
                      else n.right
        n.parent.replace_child(n, replacement)
        if n.is_black:
            if replacement.is_red:
                replacement.colour = BLACK
            else:
                replacement.colour = BLACK
                fix_double_black(replacement)

def fix_double_black(node):
    # Only the *real* root doesn't have a
    # grandparent, and if we reach there we
    # are done.
    while node.grandparent:

        if node.sibling.is_red:
            # Case 1 (sibling red means parent black)
            p = node.parent
            node.sibling.rotate()
            node.parent.colour = RED
            node.grandparent.colour = BLACK
            node.parent = p
            continue

        # If we are here, we are in case 2, 3, or 4

        if node.sibling.outer_child.is_red:
            # Case 4
            node.sibling.colour = node.parent.colour
            node.parent.colour = BLACK
            node.sibling.outer_child.colour = BLACK
            node.sibling.rotate()
            return # Done

        # Now we know that the sibling's outer child
        # is black, so we can check the inner to see if
        # we are in case 3
        if node.sibling.inner_child.is_red:
            # Case 3
            p = node.parent
            node.sibling.colour = RED
            node.sibling.inner_child.colour = BLACK
            node.sibling.inner_child.rotate()
            node.parent = p
            continue

        # We must be in Case 2
        node.sibling.colour = RED
        if node.parent.is_red:
            node.parent.colour = BLACK
            return # Done
        else:
            node.parent.colour = BLACK
            node = node.parent
            continue

def tree_iter(node):
    if node is EMPTY_TREE:
        return
    yield from tree_iter(node.left)
    yield node.value
    yield from tree_iter(node.right)

class Greater(object):
    def __lt__(self, other):
        return False
    def __eq__(self, other):
        return False
    def __gt__(self, other):
        return True

class RedBlackSearchTreeSet(object):
    def __init__(self, seq = ()):
        self.tree = Tree(Greater(), BLACK)
        for value in seq:
            self.add(value)

    def add(self, val):
        insert(self.tree, val)
        self.tree.left.colour = BLACK

    def remove(self, val):
        remove(self.tree, val)
        self.tree.left.colour = BLACK

    def __iter__(self):
        return tree_iter(self.tree.left)

    def __contains__(self, element):
        return contains(self.tree, element)

    def __repr__(self):
        return 'RedBlackSearchTreeSet(tree_iter(' + \
                repr(self.tree.left) + '))'



tree = RedBlackSearchTreeSet([1, 2, 3, 4, 5, 7, 8, 9])
for i in range(10):
    print(i in tree)
tree.add(0)
tree.remove(8)
for i in range(10):
    print(i in tree)
