class Counter(object):
    def __init__(self):
        self.counter = 0
    def tick(self):
        self.counter += 1
    def value(self):
        return self.counter
    def __repr__(self):
        return "Counter({})".format(self.counter)

c = Counter()
c.tick()
c.tick()
print(c.value())
