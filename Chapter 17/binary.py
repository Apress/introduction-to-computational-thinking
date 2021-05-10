def parent(j):
    return (j - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2

class Heap(object):
    def construct_heap(self):
        for i in reversed(range(len(self.nodes))):
            self.fix_down(i)

    def __init__(self, seq = ()):
        self.nodes = list(seq)
        self.construct_heap()

    def is_empty(self):
        return len(self.nodes) == 0

    def __bool__(self):
        return not self.is_empty()

    def get_min(self):
        return self.nodes[0]

    def fix_up(self, j):
        n = self.nodes # for shorter notation
        while j > 0:
            i = parent(j)
            if n[j] >= n[i]:
                # we satisfy the heap
                # property so we are done
                break
            # flip values
            n[i], n[j] = n[j], n[i]
            j = i # continue from parent

    def add(self, x):
        self.nodes.append(x)
        self.fix_up(len(self.nodes) - 1)

    def fix_down(self, i):
        n = self.nodes # for shorter notation
        while i < len(self.nodes):
            j, k = left(i), right(i)

            if j >= len(self.nodes):
                break # we don't have children, so done

            if k >= len(self.nodes):
                # we have a left child but not a right
                if n[i] > n[j]:
                    n[i], n[j] = n[j], n[i]
                break # done

            if n[i] <= n[j] and n[i] <= n[k]:
                # children are larger, so we are done
                break

            # flip with the smallest
            if n[j] < n[k]:
                n[i], n[j] = n[j], n[i]
                i = j
            else:
                n[i], n[k] = n[k], n[i]
                i = k

    def delete_min(self):
        m = self.nodes[0]
        last = self.nodes.pop()
        if self.nodes:
            self.nodes[0] = last
            self.fix_down(0)
        return m

    def __repr__(self):
        return 'Heap(' + repr(self.nodes) + ')'

def heapsort(x):
    heap = Heap(x)
    res = []
    while heap:
        res.append(heap.delete_min())
    return res

x = [1, 2, 7, 2, 4, 8]
print(heapsort(x))
