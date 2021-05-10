from dataclasses import dataclass
from stack import Stack

@dataclass
class Node:
    value: object
    left: Node = None
    right: Node = None

def tree_iter(node):
    if node is None: return
    yield from tree_iter(node.left)
    yield node.value
    yield from tree_iter(node.right)

tree = Node(1, Node(2, None, None), Node(3, Node(4), Node(5)))
print(tree)
print(list(tree_iter(tree)))


class TreeIterator(object):
    def __init__(self, tree):
        self.stack = Stack()
        self.stack.push(tree)

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.stack:
            x = self.stack.pop()
            if x is None:
                continue # return to next stack frame
            if type(x) is Node:
                self.stack.push(x.right)
                self.stack.push(x.value)
                self.stack.push(x.left)
            else:
                return x
        raise StopIteration()

print(list(TreeIterator(tree)))
