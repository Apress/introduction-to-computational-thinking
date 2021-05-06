class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
    def __repr__(self):
        return 'Link({}, {})'.format(
            repr(self.element),
            repr(self.next)
        )
        
class DoublyLink(object):
    def __init__(self, element, previous, next):
        self.element = element
        self.previous = previous
        self.next = next
    def __repr__(self):
        return 'DoublyLink({}, {})'.format(
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



# In the code below I have removed the functionality we do not need for
# the iterators. The methods that are missing are identical to those in the
# other files.

class ListSequence(object):
    def __init__(self, seq = ()):
        self.sequence = list(seq)

    def __iter__(self):
        # Get the elements from the underlying sequence
        yield from self.sequence

    def __repr__(self):
        return f"ListSequence({self.sequence})"


class LinkedListSequence(object):
    def __init__(self, seq = ()):
        self.dummy = Link(None, None)
        self.last = self.dummy
        for x in seq:
            self.append(x)

    def append(self, element):
        self.last.next = Link(element, None)
        self.last = self.last.next

    def __iter__(self):
        link = self.dummy.next
        while link:
            yield link.element
            link = link.next

    def __repr__(self):
        return f"LinkedListSequence({list(self)})"


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

    def __iter__(self):
        link = self.first.next
        while link is not self.last:
            yield link.element
            link = link.next

    def __repr__(self):
        return f"DoublyLinkedListSequence({list(self)})"

seq1 = ListSequence(range(5))
seq2 = LinkedListSequence(range(5))
seq3 = DoublyLinkedListSequence(range(5))

print(seq1, seq2, seq3)
# The list() constructor creates a list from the sequences iterators
print(list(seq1), list(seq2), list(seq3))
