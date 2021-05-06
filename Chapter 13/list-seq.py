class ListSequence(object):
    def __init__(self, seq = ()):
        self.sequence = list(seq)

    def append(self, element):
        self.sequence.append(element)

    def prepend(self, element):
        self.sequence.insert(0, element)

    def remove_first(self):
        self.sequence.pop(0)

    def remove_last(self):
        self.sequence.pop()

    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index")
        return self.sequence[index]

    def set_at_index(self, index, value):
        if index < 0:
            raise IndexError("Negative index")
        self.sequence[index] = value

    def extend(self, other):
        self.sequence.extend(other.sequence)

    def __repr__(self):
        return repr(self.sequence)

seq = ListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)

seq2 = ListSequence(range(6,10))
seq.extend(seq2)
print(seq)
seq.remove_first()
print(seq)
seq.prepend(-1)
print(seq)
seq.remove_last()
print(seq)