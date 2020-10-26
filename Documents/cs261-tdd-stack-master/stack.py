# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:
    def __init__(self):
        self.data = []
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def pop(self):
        if self.is_empty():
            raise IndexError
        self.size -= 1
        return self.data.pop(self.size)
