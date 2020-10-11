# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
DEFAULT_CAPACITY = 10
class DynamicArray:
    def __init__(self):
        self.data = []
        self.capacity = DEFAULT_CAPACITY
        self.size = 0
    

    def is_empty(self):
        return self.data == []
