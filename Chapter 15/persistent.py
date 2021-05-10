RED = 0
BLACK = 1
DOUBLE_BLACK = 2

class Node(object):
    def __init__(self,
				 value,
                 colour,
                 left,
                 right):
        self.value = value
        self.colour = colour
        self.left = left
        self.right = right

        if (self.left is None) != (self.right is None):
            raise TypeError("Either both or neither subtree can be None")

    def is_empty(self):
        return self.left is None

    def __repr__(self):
        return 'Node({}, {}, left = {}, right = {})'.format(
            repr(self.value),
            repr(self.colour),
            repr(self.left),
            repr(self.right)
        )

EmptyTree = Node(None, BLACK, None, None)
DoubleBlackEmptyTree = Node(None, DOUBLE_BLACK, None, None)

def contains(node, value):
    if node.is_empty():
        return False
    if node.value == value:
        return True
    if node.value > value:
        return contains(node.left, value)
    if node.value < value:
        return contains(node.right, value)

def tree_iter(node):
    if node.is_empty():
        return
    yield from tree_iter(node.left)
    yield node.value
    yield from tree_iter(node.right)

class MatchError(Exception):
    pass

def collect_extraction(node, parent, code_lines):
    if type(node) is str:
        code_lines.append(
            "{} = {}".format(node, parent)
        )
        return code_lines

    code_lines.extend([
        '{} = {}'.format(node.value, parent),
        'if {}.colour != {}: raise MatchError()'.format(
            node.value, node.colour
        )
    ])
    collect_extraction(node.left,
                       node.value + ".left",
                       code_lines)
    collect_extraction(node.right,
                       node.value + ".right",
                       code_lines)
    code_lines.append(
        '{0} = {0}.value'.format(node.value)
    )
    return code_lines

class FunctionCall(object):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Function(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, dsl_expr):
        return FunctionCall(self.name, dsl_expr)

Balance = Function("balance")

def output_string(output):
    if type(output) is str:
        return output

    if type(output) is FunctionCall:
        return output.name + '(' + output_string(output.expr) + ')'

    return 'Node(' + output.value + ', '               \
                   + str(output.colour) + ', '         \
                   + output_string(output.left) + ', ' \
                   + output_string(output.right) + ')'

def transformation_rule(input, output):
    body_lines = collect_extraction(input, 'tree', [])
    body = "\n\t\t".join(body_lines)
    ret = "return {}".format(output_string(output))
    func = '\n'.join([
        "def rule(tree):",
        "\ttry:",
        '\t\t' + body,
        '\t\t' + ret,
        "\texcept AttributeError:",
        "\t\traise MatchError()"
    ])
    defs = {}
    exec(func, globals(), defs)
    return defs["rule"]


def mirror(tree):
    if type(tree) is str:
        return tree
    elif type(tree) is FunctionCall:
        func = Function(tree.name)
        return func(mirror(tree.expr))
    else:
        return Node(tree.value, tree.colour,
                    mirror(tree.right),
                    mirror(tree.left))


top_case = \
    Node("z", BLACK,
         Node("x", RED,
              "a",
              Node("y", RED, "b", "c")),
        "d")
left_case = \
    Node("z", BLACK,
         Node("y", RED,
              Node("x", RED, "a", "b"),
              "c"),
         "d")
to_pattern = \
    Node("y", RED,
         Node("x", BLACK, "a", "b"),
         Node("z", BLACK, "c", "d"))

transformations = [
    transformation_rule(top_case, to_pattern),
    transformation_rule(mirror(top_case), mirror(to_pattern)),
    transformation_rule(left_case, to_pattern),
    transformation_rule(mirror(left_case), mirror(to_pattern))
]

from_double_black = \
    Node("z", DOUBLE_BLACK,
         Node("x", RED,
              "a",
              Node("y", RED, "b", "c")),
        "d")
to_double_black = \
    Node("y", BLACK,
        Node("x", BLACK, "a", "b"),
        Node("z", BLACK, "c", "d"))

transformations.extend([
    transformation_rule(from_double_black, to_double_black),
    transformation_rule(mirror(from_double_black), mirror(to_double_black))
])

def balance(tree):
    for rule in transformations:
        try:
            return rule(tree)
        except MatchError:
            pass
    # None of the patterns matched, so return the tree
    return tree

def insert_rec(node, value):
    if node.is_empty():
        return Node(value, RED, EmptyTree, EmptyTree)

    if node.value == value:
        return node

    elif node.value > value:
        new_tree = Node(node.value, node.colour,
                        left = insert_rec(node.left, value),
                        right = node.right)
        return balance(new_tree)

    elif node.value < value:
        new_tree = Node(node.value, node.colour,
                        left = node.left,
                        right = insert_rec(node.right, value))
        return balance(new_tree)

def insert(node, value):
    new_tree = insert_rec(node, value)
    new_tree.colour = BLACK
    return new_tree

first_row_from = \
    Node("y", RED,
         Node("x", DOUBLE_BLACK, "a", "b"),
         Node("z", BLACK, "c", "d"))
first_row_to = \
    Balance(
        Node("z", BLACK,
             Node("y", RED,
                  Node("x", BLACK, "a", "b"),
                  "c"),
             "d"))

second_row_from = \
    Node("y", BLACK,
         Node("x", DOUBLE_BLACK, "a", "b"),
         Node("z", BLACK, "c", "d"))
second_row_to = \
    Balance(Node("z", DOUBLE_BLACK,
                 Node("y", RED,
                      Node("x", BLACK, "a", "b"),
                      "c"),
                 "d"))

third_row_from = \
    Node("x", BLACK,
         Node("w", DOUBLE_BLACK, "a", "b"),
         Node("z", RED,
              Node("y", BLACK, "c", "d"),
              "e"))
third_row_to = \
    Node("z", BLACK,
         Balance(
            Node("y", BLACK,
                 Node("x", RED,
                      Node("w", BLACK, "a", "b"),
                      "c"),
                 "d")
         ),
         "e")

rotations = [
    # First row
    transformation_rule(
        first_row_from, first_row_to
    ),
    transformation_rule(
        mirror(first_row_from), mirror(first_row_to)
    ),

    # Second row
    transformation_rule(
        second_row_from, second_row_to
    ),
    transformation_rule(
        mirror(second_row_from), mirror(second_row_to)
    ),

    # Third row
    transformation_rule(
        third_row_from, third_row_to
    ),
    transformation_rule(
        mirror(third_row_from), mirror(third_row_to)
    )
]

def rotate_balance(tree):
    for rule in rotations:
        try:
            return rule(tree)
        except MatchError:
            pass
    # None of the patterns matched, so return the tree
    return tree

def rightmost_value(node):
    if node.right.is_empty():
        return node.value
    else:
        return rightmost_value(node.right)

def remove_rec(node, value):
    if node.is_empty():
		# if we get to an empty tree, it means
		# that we couldn't find the value in the
		# tree
        raise KeyError()

    if node.value > value:
        new_tree = Node(node.value,
                        node.colour,
                        left = remove_rec(node.left, value),
                        right = node.right)
        return rotate_balance(new_tree)

    if node.value < value:
        new_tree = Node(node.value,
                        node.colour,
                        left = node.left,
                        right = remove_rec(node.right, value))
        return rotate_balance(new_tree)

    # we have value == node.value
    if node.left.is_empty() and node.right.is_empty():
        if node.colour is RED:
            return EmptyTree
        else:
            return DoubleBlackEmptyTree

    if node.left.is_empty():
        return Node(node.right.value, BLACK,
                    node.right.left, node.right.right)

    if node.right.is_empty():
        return Node(node.left.value, BLACK,
                    node.left.left, node.left.right)

    # general case removal
    replacement = rightmost_value(node.left)
    new_tree = Node(replacement, node.colour,
                    remove_rec(node.left, replacement),
                    node.right)

    return rotate_balance(new_tree)

def remove(tree, value):
    new_tree = remove_rec(tree, value)
    new_tree.colour = BLACK
    return new_tree


class RedBlackSearchTreeSet(object):
    def __init__(self, seq = ()):
        self.tree = EmptyTree
        for value in seq:
            self.add(value)

    def add(self, element):
        self.tree = insert(self.tree, element)

    def remove(self, element):
        self.tree = remove(self.tree, element)

    def __iter__(self):
        return tree_iter(self.tree)

    def __contains__(self, element):
        return contains(self.tree, element)

    def __repr__(self):
        return 'RedBlackSearchTreeSet(tree_iter(' + repr(self.tree) + '))'


tree = RedBlackSearchTreeSet([1, 2, 3, 4, 5, 7, 8, 9])
for i in range(10):
    print(i in tree)
tree.add(0)
tree.remove(8)
for i in range(10):
    print(i in tree)
