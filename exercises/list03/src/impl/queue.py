class QueueEmptyException(Exception):
    pass

class Queue:
    def __init__(self, items = None):
        self.items = items or []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException()
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException()
        return self.items[0]

    def size(self):
        return len(self.items)
