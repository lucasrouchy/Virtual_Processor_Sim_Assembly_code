# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self
    def is_sentinel(self):
        return self.value == None 
    def is_empty(self):
        return self.next == self and self.prev == self
    def is_last(self):
        return self == self.last()
    def last(self): 
        if self.is_empty():
            return self
        elif self.next.is_sentinel():
            return self
        else:
            return self.next.last()
    def append(self, new_node):
        self.last().insert(new_node)
    def insert(self, new_node):
        new_node.next = self.next
        new_node.prev = self
        self.next.prev = new_node
        self.next = new_node    
    def insert_in_order(self, new_node):
        if self.is_empty():
            return self.append(new_node)
        elif self.next == self.last().next:
            return self.insert(new_node)
        elif self.next.value > new_node.value:
            return self.insert(new_node)
        else:
            return self.next.insert_in_order(new_node)
        








    



        

   