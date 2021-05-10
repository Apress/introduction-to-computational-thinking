from dataclasses import dataclass

@dataclass
class Node(object):
    value: object
    left:  Node | None = None
    right: Node | None = None

def is_empty(heap):
    return heap is None

def get_min(heap):
    return heap.value

def add(heap, x):
    return merge(heap, Node(x))

def delete_min(heap):
    return heap.value, merge(heap.left, heap.right)

def merge(x, y):
    if x is None: return y
    if y is None: return x
    if x.value < y.value:
        return Node(x.value, x.left, merge(x.right, y))
    else:
        return Node(y.value, y.left, merge(y.right, x))

def node_iter(node):
    if node is None:
        return
    yield node.value
    yield from node_iter(node.left)
    yield from node_iter(node.right)

class Heap(object):
    def __init__(self, seq = ()):
        self.heap = None
        for x in seq:
            self.add(x)

    def is_empty(self):
        return is_empty(self.heap)

    def __bool__(self):
        return not self.is_empty()

    def add(self, x):
        self.heap = add(self.heap, x)

    def get_min(self):
        return get_min(self.heap)

    def delete_min(self):
        res, self.heap = delete_min(self.heap)
        return res

    def __repr__(self):
        return 'Heap(' + repr(list(node_iter(self.heap))) + ')'


def heapsort(x):
    heap = Heap(x)
    res = []
    while heap:
        res.append(heap.delete_min())
    return res

x = [1, 2, 7, 2, 4, 8]
print(heapsort(x))
