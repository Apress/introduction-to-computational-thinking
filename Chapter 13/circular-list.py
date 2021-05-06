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
        # Use a single dummy head here. It is both ends of the list
        self.head = DoublyLink(None, None, None)
        self.head.next = self.head
        self.head.previous = self.head
        for x in seq:
            self.append(x)

    def append(self, element):
        insert_after(self.head.previous, element)

    def prepend(self, element):
        insert_after(self.head, element)

    def get_link(self, index):
        if index < 0:
            raise IndexError("Negative index")
        link = self.head.next
        while link is not self.head:
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
        insert_list_after(self.head.previous,
                          other.head.next,
                          other.head.previous)

    def insert_sequence_at(self, index, other):
        link = self.get_link(index)
        insert_list_after(link,
                          other.head.next,
                          other.head.previous)

    def remove_first(self):
        if self.head.next == self.head:
            raise IndexError("Empty sequence")
        remove_link(self.head.next)

    def remove_last(self):
        if self.head.next == self.head:
            raise IndexError("Empty sequence")
        remove_link(self.head.previous)

    def __repr__(self):
        x = []
        link = self.head.next
        while link is not self.head:
            x.append(link.element)
            link = link.next
        return f"DoublyLinkedListSequence({x})"

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
