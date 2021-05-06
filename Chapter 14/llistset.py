class Link(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next
    def __repr__(self):
        return 'Link({}, {})'.format(
            repr(self.element),
            repr(self.next)
        )

def contains(links, element):
    if links is None:
        return False
    if links.element == element:
        return True
    return contains(links.next, element)

def remove(links, element):
    if links is None:
        raise KeyError()
    if links.element == element:
        return links.next
    return Link(links.element, remove(links.next, element))

def link_iterator(links):
    link = links
    while link is not None:
        yield link.element
        link = link.next

class LinkedListSet(object):
    def __init__(self, seq = ()):
        self.links = None
        for element in seq:
            self.add(element)

    def add(self, element):
        if not element in self:
            self.links = Link(element, self.links)

    def remove(self, element):
        self.links = remove(self.links, element)

    def __iter__(self):
        return link_iterator(self.links)

    def __contains__(self, element):
        return contains(self.links, element)

    def __repr__(self):
        return 'LinkedListSet(link_iterator(' + repr(self.links) + '))'

x = LinkedListSet([1,2,1,4])
print(x)
for i in range(5):
    print(f"is {i} in {x}? {i in x}")
