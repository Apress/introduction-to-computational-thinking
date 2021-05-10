from dataclasses import dataclass

@dataclass
class BT:
    value: object
    rank: int = 0
    sibling:  BT | None = None
    children: BT | None = None

def sib(x, y):
    # prepend x to y's sibling list (returns new node)
    return BT(x.value, x.rank, sibling = y, children = x.children)

def link(x, y):
    # link one tree as the first child of another
    assert x.rank == y.rank
    if x.value < y.value:
        return BT(x.value, x.rank + 1, children = sib(y, x.children))
    else:
        return BT(y.value, y.rank + 1, children = sib(x, y.children))

def insert_tree(t, trees):
    # trees must be sorted in non-decreasing order.
    # t cannot have larger rank than trees.
    if trees is None: return t
    if t.rank < trees.rank:
        return sib(t, trees)
    else:
        return insert_tree(link(t, trees), trees.sibling)

def get_smallest(trees):
    # trees must be non-empty
    x = trees
    y = trees.sibling
    while y is not None:
        if y.value < x.value:
            x = y
        y = y.sibling
    return x

def get_min(trees):
    return get_smallest(trees).value

def merge(x, y):
    # x and y must be sorted in non-decreasing rank.
    if x is None: return y
    if y is None: return x
    if x.rank < y.rank:
        return sib(x, merge(x.sibling, y))
    elif x.rank > y.rank:
        return sib(y, merge(x, y.sibling))
    else: # x.rank == y.rank:
        return insert_tree(link(x, y), merge(x.sibling, y.sibling))

def delete_tree(t, trees):
    if trees is None: return None
    if trees == t: return trees.sibling
    trees.sibling = delete_tree(t, trees.sibling)
    return trees

def reverse_trees(x):
    res = None
    while x:
        res = sib(x, res)
        x = x.sibling
    return res

def delete_min(trees):
    t = get_smallest(trees)
    trees = delete_tree(t, trees)
    return merge(reverse_trees(t.children), trees)

class Heap(object):
    def __init__(self, seq = ()):
        self.trees = None
        self.min = None
        for x in seq: # This is O(n), see below
            self.add(x)

    def is_empty(self):
        return self.trees is None

    def __bool__(self):
        return not self.is_empty()

    def get_min(self):
        return self.min

    def add(self, x):
        if self.min is None or x < self.min:
            self.min = x
        self.trees = insert_tree(BT(x), self.trees)

    def delete_min(self):
        t = get_smallest(self.trees)
        min_val = t.value
        self.trees = delete_tree(t, self.trees)
        self.trees = merge(reverse_trees(t.children), self.trees)
        # cache new min value
        if not self.is_empty():
            t = get_smallest(self.trees)
            self.min = t.value
        return min_val


def heapsort(x):
    heap = Heap(x)
    res = []
    while heap:
        res.append(heap.delete_min())
    return res

x = [1, 2, 7, 2, 4, 8]
print(heapsort(x))
