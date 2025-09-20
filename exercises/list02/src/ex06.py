class StackInvalidCapacityException(Exception):
    pass

class StackInvalidValueException(Exception):
    pass

class StackUnderflowException(Exception):
    pass

class StackOverflowException(Exception):
    pass

class BoundedStack:
    def __init__(self, capacity = 1):
        if not isinstance(capacity, int) or capacity < 1:
            raise StackInvalidCapacityException()

        self.values = []
        self.capacity = capacity
    
    def size(self):
        return len(self.values)

    def is_empty(self):
        return self.size() == 0
    
    def is_full(self):
        return self.size() == self.capacity

    def push(self, value):
        if self.is_full():
            raise StackOverflowException()

        if not isinstance(value, int) or value < 0:
            raise StackInvalidValueException()

        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowException()

        return self.values.pop()

    def peek(self):
        if self.is_empty():
            raise StackUnderflowException()

        return self.values[-1]

    def clear(self):
        self.values.clear()
