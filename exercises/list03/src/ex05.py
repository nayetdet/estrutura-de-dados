from impl.stack import Stack

class StackBasedQueueEmptyException(Exception):
    pass

class StackBasedQueue:
    def __init__(self):
        self.stack = Stack()
        self.invstack = Stack()

    def is_empty(self):
        return self.stack.is_empty() and self.invstack.is_empty()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        if self.is_empty():
            raise StackBasedQueueEmptyException()
        if self.invstack.is_empty():
            while not self.stack.is_empty():
                self.invstack.push(self.stack.pop())
        return self.invstack.pop()

    def peek(self):
        if self.is_empty():
            raise StackBasedQueueEmptyException()
        if self.invstack.is_empty():
            while not self.stack.is_empty():
                self.invstack.push(self.stack.pop())
        return self.invstack.peek()

    def size(self):
        return self.stack.size() + self.invstack.size()
