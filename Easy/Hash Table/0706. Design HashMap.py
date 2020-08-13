# Design a HashMap without using any built-in hash table libraries

# I use array's index to save keys 

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Hash=[None]*1000000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.Hash[key]=value
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.Hash[key]!= None:
            return self.Hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.Hash[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# More clear and readable with dic

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {} 

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.d[key] = value #just save key and values in dic, it will not be negative number of values

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.d:
            return self.d[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.d:
            del self.d[key] 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
