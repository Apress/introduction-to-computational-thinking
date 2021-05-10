class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            raise EmptyStack()

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise EmptyStack()

    def is_empty(self):
        return len(self.stack) == 0

    def __bool__(self):
        return not self.is_empty()
