class StackInvalidCapacityException(Exception):
    pass

class StackInvalidValueException(Exception):
    pass

class StackUnderflowException(Exception):
    pass

class StackOverflowException(Exception):
    pass

class MultiBoundedNegativeStack:
    def __init__(self, capacity=1):
        if not isinstance(capacity, int) or capacity < 1:
            raise StackInvalidCapacityException()

        self.values = [None] * capacity
        self.capacity = capacity
        self.left_idx = -1
        self.right_idx = capacity

    def size(self):
        return (self.left_idx + 1) + (self.capacity - self.right_idx)

    def is_empty_left(self):
        return self.left_idx == -1

    def is_empty_right(self):
        return self.right_idx == self.capacity

    def is_empty(self):
        return self.is_empty_left() and self.is_empty_right()

    def is_full(self):
        return self.left_idx + 1 == self.right_idx

    def left_push(self, value):
        if self.is_full():
            raise StackOverflowException()

        if not isinstance(value, int) or value >= 0:
            raise StackInvalidValueException()

        self.left_idx += 1
        self.values[self.left_idx] = value

    def left_pop(self):
        if self.is_empty_left():
            raise StackUnderflowException()

        value = self.values[self.left_idx]
        self.values[self.left_idx] = None
        self.left_idx -= 1
        return value

    def left_peek(self):
        if self.is_empty_left():
            raise StackUnderflowException()

        return self.values[self.left_idx]

    def right_push(self, value):
        if self.is_full():
            raise StackOverflowException()

        if not isinstance(value, int) or value >= 0:
            raise StackInvalidValueException()

        self.right_idx -= 1
        self.values[self.right_idx] = value

    def right_pop(self):
        if self.is_empty_right():
            raise StackUnderflowException()

        value = self.values[self.right_idx]
        self.values[self.right_idx] = None
        self.right_idx += 1
        return value

    def right_peek(self):
        if self.is_empty_right():
            raise StackUnderflowException()

        return self.values[self.right_idx]

    def clear(self):
        self.values = [None] * self.capacity
        self.left_idx = -1
        self.right_idx = self.capacity
