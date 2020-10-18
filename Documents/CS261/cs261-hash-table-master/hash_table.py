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
        if (duplicate_key := self.__get_kv_pair(key, bucket)):
            duplicate_key[1] = value
            return
        bucket.append([key, value])
        
    def __get_bucket(self, key):
        return self.data[self.hash(key)]
    def hash(self, key):
        return hash(key) % self.size
        
    def __getitem__(self, key):
        if (x := self.__get_bucket(key)) != []:
            return x[0][1]
        return None
    def __get_kv_pair(self, key, bucket):
        return next((kv_pair for kv_pair in bucket if kv_pair[0] == key), None)
    def keys(self):
        return ([kv_pair[0] for bucket in self.data for kv_pair in bucket]) 

    def values(self):
        return ([kv_pair[1] for bucket in self.data for kv_pair in bucket]) 
    def delete(self, key):
        for i, kv in enumerate(bucket := self.__get_bucket(key)):
            if kv[0] == key:
                bucket.pop(i)
    def clear(self):
        self.data = [[] for i in range(self.size)]