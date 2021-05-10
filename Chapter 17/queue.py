# Queue using lists.
class Queue(object):
    def __init__(self):
        self.front = []
        self.back = []

    def is_empty(self):
        return len(self.front) == 0 and \
                len(self.back) == 0

    def __bool__(self):
        return not self.is_empty()

    def enqueue(self, x):
        self.back.append(x)

    def move_list(self):
        if len(self.front) == 0:
            self.front = self.back
            self.front.reverse()
            self.back = []

    def front(self):
        if self.is_empty():
            raise EmptyQueue()
        self.move_list()
        return self.front[-1]

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue()
        self.move_list()
        return self.front.pop()

# Queue with wrap-around-arithmetic
class Queue(object):
    def __init__(self, capacity = 10):
        self.data = [None] * capacity
        self.used = 0
        self.front_idx = 0

    @property
    def capacity(self):
        return len(self.data)

    @property
    def back_idx(self):
        return (self.front_idx + self.used) % self.capacity

    def is_empty(self):
        return self.used == 0

    def __bool__(self):
        return not self.is_empty()

    def resize(self):
        self.data = self.data[self.front_idx:] + \
                    self.data[:self.front_idx] + \
                    [None] * self.used
        self.front_idx = 0

    def enqueue(self, x):
        if self.used == self.capacity:
            self.resize()
        self.data[self.back_idx] = x
        self.used += 1

    def front(self):
        if self.is_empty(): raise EmptyQueue()
        return self.data[self.front_idx]

    def dequeue(self):
        val = self.front()
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.used -= 1
        return val
