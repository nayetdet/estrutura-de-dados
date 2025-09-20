class StackEmptyException(Exception):
    pass

class Stack:
    def __init__(self, items = None):
        self.values = items or []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException()
        return self.values.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyException()
        return self.values[-1]
