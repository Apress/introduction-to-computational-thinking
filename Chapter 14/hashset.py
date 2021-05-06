def next_power_of_two(n):
    # Not the most efficient solution
    # but probably the simplest
    power = 1
    while power < n:
        power *= 2
    return power

class HashTableSet(object):
    def __init__(self, seq = (), initial_size = 16):
        # we want len, which might exchaust an iterator
        seq = list(seq)

        # Make sure we don't resize while we insert the
        # initial sequence
        if 2 * len(seq) > initial_size:
            initial_size = next_power_of_two(2 * len(seq))

        # Setting up the table
        self.size = initial_size
        self.used = 0
        self.array = [[] for _ in range(initial_size)]

        # And insert the sequence items
        for value in seq:
            self.add(value)

    def get_bin(self, element):
        hash_val = hash(element)
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for x in bin:
                self.add(x)

    def add(self, element):
        bin = self.get_bin(element)
        if element not in bin:
            bin.append(element)
            self.used += 1
            if self.used > self.size / 2:
                self.resize(int(2 * self.size))

    def remove(self, element):
        bin = self.get_bin(element)
        if element not in bin:
            raise KeyError()
        bin.remove(element)
        self.used -= 1
        if self.used < self.size / 4:
            self.resize(int(self.size / 2))

    def __iter__(self):
        for bin in self.array:
            yield from bin

    def __contains__(self, element):
        bin = self.get_bin(element)
        return element in bin

    def __repr__(self):
        return 'HashTableSet(' + repr(list(iter(self))) + ')'

x = HashTableSet([1,2,1,4])
print(x)
for i in range(5):
    print(f"is {i} in {list(x)}? {i in x}")
x.remove(2)
print(x)
for i in range(5):
    print(f"is {i} in {list(x)}? {i in x}")
print()
