class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, key: int) -> None:
        
        if key not in self.d:
            self.d[key] = 1
        else:
            self.d[key] += 1

    def remove(self, key: int) -> None:
        
        if key in self.d:
            del self.d[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.d 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

