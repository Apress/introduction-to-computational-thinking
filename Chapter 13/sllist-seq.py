# The code that requires Python 3.7 and up also requires
# these. If you have an older Python, delete these imports
# and remove the dataclass version below.
from dataclasses import dataclass
from typing import Union

class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
    def __repr__(self):
        return 'Link({}, {})'.format(
            repr(self.element),
            repr(self.next)
        )

# From Python 3.7 and up you could also use links as:
@dataclass
class Link(object):
    element: object
    next: Union[Link,None] # From Python 3.10 you could write next: Link | None instead


# Linked lists functions
def append(link, element):
    if link is None:
        return Link(element, None)
    else:
        return Link(link.element,
                    append(link.next, element))

def get_at_index(link, index):
    if link is None:
        raise IndexError("Index out of bounds")
    if index == 0:
        return link.element
    return get_at_index(link.next, index - 1)

def set_at_index(link, index, value):
    if link is None:
        raise IndexError("Index out of bounds")
    if index == 0:
        link.element = value
    else:
        set_at_index(link.next, index - 1, value)

# From Python 3.10 you can also write
@dataclass
class Link(object):
    element: object
    next: Link | None

def append(link, element):
    match link:
        case None:      return Link(element, None)
        case Link(e,n): return Link(e, append(n, element))

def get_at_index(link, index):
    match link:
        case None:      raise IndexError("Index out of bounds")
        case Link(e,n): return e if index == 0 else get_at_index(n, index - 1)

def set_at_index(link, index, value):
    match link:
        case None:
            raise IndexError("Index out of bounds")
        case Link(e,n):
            if index == 0:
                link.element = value
            else:
                set_at_index(n, index - 1, value)


llist = Link(1, Link(2, Link(3, None)))
print(llist)
llist = append(llist, 4)
print(llist)
print(get_at_index(llist, 2))
set_at_index(llist, 2, 42)
print(get_at_index(llist, 2))
print(llist)


class LinkedListSequence(object):
    def __init__(self, seq = ()):
        # Inefficient, but worry about that for another day...
        self.links = None
        for x in seq:
            self.links = append(self.links, x)

    def append(self, element):
        self.links = append(self.links, element)

    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index")
        return get_at_index(self.links, index)

    def set_at_index(self, index, value):
        if index < 0:
            raise IndexError("Negative index")
        set_at_index(self.links, index, value)

    def __repr__(self):
        return repr(self.links)

seq = LinkedListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)


# Iterative solution
class LinkedListSequence(object):
    def __init__(self, seq = ()):
        self.links = None
        self.last = None
        for x in seq:
            self.append(x)

    def append(self, element):
        if self.links is None:
            self.links = Link(element, None)
            self.last = self.links
            return
        self.last.next = Link(element, None)
        self.last = self.last.next

    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index")
        link = self.links
        while link is not None:
            if index == 0:
                return link.element
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def set_at_index(self, index, value):
        if index < 0:
            raise IndexError("Negative index")
        link = self.links
        while link is not None:
            if index == 0:
                link.element = value
                return
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def __repr__(self):
        return repr(self.links)


seq = LinkedListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)



# Adding dummy element
class LinkedListSequence(object):
    def __init__(self, seq = ()):
        self.dummy = Link(None, None)
        self.last = self.dummy
        for x in seq:
            self.append(x)

    def append(self, element):
        self.last.next = Link(element, None)
        self.last = self.last.next

    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index")
        link = self.dummy.next
        while link is not None:
            if index == 0:
                return link.element
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def set_at_index(self, index, value):
        if index < 0:
            raise IndexError("Negative index")
        link = self.dummy.next
        while link is not None:
            if index == 0:
                link.element = value
                return
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def __repr__(self):
        return repr(self.dummy.next)


seq = LinkedListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)


# Extending with additional methods
class LinkedListSequence(object):
    def __init__(self, seq = ()):
        self.dummy = Link(None, None)
        self.last = self.dummy
        for x in seq:
            self.append(x)

    def append(self, element):
        self.last.next = Link(element, None)
        self.last = self.last.next

    def prepend(self, element):
        new_link = Link(element, self.dummy.next)
        if self.last == self.dummy:
            self.last = new_link
        self.dummy.next = new_link

    def remove_first(self):
        if self.dummy.next is None:
            raise IndexError("Empty sequence")
        self.dummy.next = self.dummy.next.next
        if self.dummy.next is None:
            self.last = self.dummy

    def remove_last(self):
        if self.dummy.next is None:
            raise IndexError("Empty sequence")
        link = self.dummy
        while link.next != self.last:
            link = link.next
        link.next = None
        self.last = link
        
    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index")
        link = self.dummy.next
        while link is not None:
            if index == 0:
                return link.element
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def set_at_index(self, index, value):
        if index < 0:
            raise IndexError("Negative index")
        link = self.dummy.next
        while link is not None:
            if index == 0:
                link.element = value
                return
            link = link.next
            index -= 1
        raise IndexError("Index out of bounds")

    def extend(self, other):
        self.last.next = other.dummy.next
        if other.last != other.dummy:
            self.last = other.last

    def __repr__(self):
        return repr(self.dummy.next)

seq = LinkedListSequence(range(5))
print(seq)
seq.append(5)
print(seq)
print(seq.get_at_index(2))
seq.set_at_index(2, 42)
print(seq)

seq2 = LinkedListSequence(range(6,10))
seq.extend(seq2)
print(seq)
seq.remove_first()
print(seq)
seq.prepend(-1)
print(seq)
seq.remove_last()
print(seq)
