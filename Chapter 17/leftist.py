from dataclasses import dataclass, field
from queue import Queue

def rank(node):
    if node is None:
        return 0
    else:
        return node.rank

@dataclass
class Node(object):
    value: object
    left:  Node | None = None
    right: Node | None = None
    rank: int = -1
    def __post_init__(self):
        self.rank = rank(self.right) + 1

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
        return restore(x.value, x.left, merge(x.right, y))
    else:
        return restore(y.value, y.left, merge(y.right, x))

def restore(value, left, right):
    if rank(left) < rank(right):
        left, right = right, left
    return Node(value, left, right)

def build_heap(seq):
    queue = Queue()

    for x in seq:
        queue.enqueue(Node(x))

    while queue:
        first = queue.dequeue()
        if queue.is_empty():
            # done
            return first
        second = queue.dequeue()
        queue.enqueue(merge(first, second))

    # We can only get here if seq was empty; in that
    # case we want the empty heap, which is None
    return None

def node_iter(node):
    if node is None:
        return
    yield node.value
    yield from node_iter(node.left)
    yield from node_iter(node.right)

class Heap(object):
    def __init__(self, seq = ()):
        self.heap = build_heap(seq)

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
    print(heap.heap)
    res = []
    while heap:
        res.append(heap.delete_min())
    return res

x = [1, 2, 7, 2, 4, 8]
print(heapsort(x))
