from impl.queue import Queue

class QueueBasedStackEmptyException(Exception):
    pass

class QueueBasedStack:
    def __init__(self):
        self.queue = Queue()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, item):
        self.queue.enqueue(item)
        for _ in range(self.queue.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        if self.is_empty():
            raise QueueBasedStackEmptyException()
        return self.queue.dequeue()
    
    def peek(self):
        if self.is_empty():
            raise QueueBasedStackEmptyException()
        return self.queue.peek()

    def size(self):
        return self.queue.size()
