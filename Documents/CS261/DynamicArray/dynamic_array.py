# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
# import numpy
import numpy as np

DEFAULT_CAPACITY = 10
class DynamicArray:
    def __init__(self):
        
        self.capacity = DEFAULT_CAPACITY
        self.size = 0
        self.data = np.ndarray(self.capacity,dtype= object)
 

    
    def __len__(self):
        lenght= 0
        for object in self.data:
            if object !=None:
                lenght +=1
        return lenght

    def is_empty(self):
        if self.__len__() == 0: 
            return True
        else:
            return False
    
    def __getitem__(self, num): 
        return self.data[num]
    def append(self, value):
        self.size+=1
        if self.size > self.capacity:
            self.capacity *=2
        self.data[self.size - 1] = value
        