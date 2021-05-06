def next_power_of_two(n):
    # Not the most efficient solution
    # but probably the simplest
    power = 1
    while power < n:
        power *= 2
    return power

def get_bin_index(bin, key):
    for i, (k, v) in enumerate(bin):
        if k == key:
            return i
    return None

class HashTableDict(object):
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
        self.array = [list() for _ in range(initial_size)]

        # And insert the sequence items
        for key, val in seq:
            self[key] = val

    def get_bin(self, key):
        hash_val = hash(key)
        index = hash_val % self.size
        return self.array[index]

    def resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.used = 0
        self.array = [list() for _ in range(new_size)]
        for bin in old_array:
            for key, val in bin:
                self[key] = val

    def __setitem__(self, key, value):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            bin.append((key, value))
            self.used += 1
            if self.used > self.size / 2:
                self.resize(2 * self.size)
        else:
            bin[idx] = (key, value)

    def __getitem__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            raise KeyError(key)
        else:
            k, v = bin[idx]
            return v

    def __delitem__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        if idx is None:
            raise KeyError(key)
        else:
            bin.pop(idx)
            self.used -= 1
            if self.used < self.size / 4:
                self.resize(int(self.size / 2))

    def __contains__(self, key):
        bin = self.get_bin(key)
        idx = get_bin_index(bin, key)
        return idx is not None

    def __iter__(self):
        for bin in self.array:
            for k, v in bin:
                yield k

    def __repr__(self):
        return 'HashTableDict(' + repr(list(iter(self))) + ')'

d = HashTableDict()
d["foo"] = 42
d["bar"] = 13
print(d)
print(d["foo"], d["bar"])
del d["foo"]
print(d)
