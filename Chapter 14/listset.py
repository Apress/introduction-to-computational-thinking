class ListSet(object):
    def __init__(self, seq = ()):
        self.data = []
        for x in seq:
            self.add(x)

    def add(self, element):
        if element not in self:
            self.data.append(element)

    def remove(self, element):
        try:
            idx = self.data.index(element)
            self.data.pop(idx)
        except ValueError:
            raise KeyError()

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, element):
        for x in self.data:
            if x == element:
                return True
        return False

    def __repr__(self):
        return 'ListSet(' + repr(self.data) + ')'

x = ListSet([1,2,1,4])
print(x)
for i in range(5):
    print(f"is {i} in {x}? {i in x}")
