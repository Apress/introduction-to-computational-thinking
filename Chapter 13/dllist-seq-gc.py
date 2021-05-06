import weakref
class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.set_previous(previous)
        self.next = next

    def get_previous(self):
        if self._previous is None:
            return None
        else:
            return self._previous()

    def set_previous(self, ref):
        if ref is None:
            self._previous = None
        else:
            self._previous = weakref.ref(ref)

    previous = property(get_previous, set_previous)

    def __repr__(self):
        return 'DoubleLink({}, {})'.format(
            repr(self.element),
            repr(self.next)
        )

# This is an alternative way to set a property; use a decorator
# for the gettter and then the attribute+".setter" as a decorator
# for the setter. It does the same as the code above.
class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.previous = previous
        self.next = next

    @property
    def previous(self):
        if self._previous is None:
            return None
        else:
            return self._previous()

    @previous.setter
    def previous(self, ref):
        if ref is None:
            self._previous = None
        else:
            self._previous = weakref.ref(ref)

    def __repr__(self):
        return 'DoubleLink({}, {})'.format(
            repr(self.element),
            repr(self.next)
        )

def insert_list_after(link, begin, end):
    end.next = link.next
    end.next.previous = end
    begin.previous = link
    link.next = begin

def insert_after(link, element):
    new_link = DoublyLink(element, None, None)
    insert_list_after(link, new_link, new_link)

def remove_link(link):
    link.previous.next = link.next
    link.next.previous = link.previous

class DoublyLinkedListSequence(object):
    def __init__(self, seq = ()):
        self.first = DoublyLink(None, None, None)
        self.last = DoublyLink(None, None, None)
        self.first.next = self.last
        self.last.previous = self.first
        for x in seq:
            self.append(x)

    def append(self, element):
        insert_after(self.last.previous, element)

    def prepend(self, element):
        insert_after(self.first, element)

    def get_link(self, index):
        if index < 0:
            raise IndexError("Negative index")
        link = self.first.next
        while link is not self.last:
            if index == 0:
                return link
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")
        
    def get_at_index(self, index):
        return self.get_link(index).element

    def set_at_index(self, index, value):
        self.get_link(index).element = value

    def extend(self, other):
        insert_list_after(self.last.previous,
                          other.first.next,
                          other.last.previous)

    def insert_sequence_at(self, index, other):
        link = self.get_link(index)
        insert_list_after(link,
                          other.first.next,
                          other.last.previous)

    def remove_first(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.first.next)

    def remove_last(self):
        if self.first.next == self.last:
            raise IndexError("Empty sequence")
        remove_link(self.last.previous)

    def __repr__(self):
        return repr(self.first.next)

seq = DoublyLinkedListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)

seq2 = DoublyLinkedListSequence(range(6,10))
seq.extend(seq2)
print(seq)
seq.remove_first()
print(seq)
seq.prepend(-1)
print(seq)
seq.remove_last()
print(seq)
