from impl.stack import Stack

class StackBasedDequeEmptyException(Exception):
    pass

class StackBasedDeque:
    def __init__(self):
        self.stack = Stack()
        self.invstack = Stack()

    def is_empty(self):
        return self.stack.is_empty() and self.invstack.is_empty()

    def add_front(self, item):
        self.invstack.push(item)

    def add_rear(self, item):
        self.stack.push(item)

    def remove_front(self):
        if self.is_empty():
            raise StackBasedDequeEmptyException()
        if self.invstack.is_empty():
            while not self.stack.is_empty():
                self.invstack.push(self.stack.pop())
        return self.invstack.pop()

    def remove_rear(self):
        if self.is_empty():
            raise StackBasedDequeEmptyException()
        if self.stack.is_empty():
            while not self.invstack.is_empty():
                self.stack.push(self.invstack.pop())
        return self.stack.pop()

    def peek_front(self):
        if self.is_empty():
            raise StackBasedDequeEmptyException()
        if self.invstack.is_empty():
            while not self.stack.is_empty():
                self.invstack.push(self.stack.pop())
        return self.invstack.peek()

    def peek_rear(self):
        if self.is_empty():
            raise StackBasedDequeEmptyException()
        if self.stack.is_empty():
            while not self.invstack.is_empty():
                self.stack.push(self.invstack.pop())
        return self.stack.peek()

    def size(self):
        return self.stack.size() + self.invstack.size()
