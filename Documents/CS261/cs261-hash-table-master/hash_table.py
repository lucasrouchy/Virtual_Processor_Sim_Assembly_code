# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(size)]
    
    def __setitem__(self, key, value):
        bucket=self.__get_bucket(key)
        
    def __get_bucket(self, key):
        return self.data[self.hash(key)]
    def hash(self, key):
        return hash(key) % self.size
        
    def __getitem__(self, key):
        if (x := self.__get_bucket(key)) != []:
            return x[0][1]
        return None
