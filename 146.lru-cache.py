#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        self.capacity = capacity
        self.ordereddict = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.ordereddict:
            return -1
        res = self.ordereddict[key]
        self.ordereddict.move_to_end(key, last = False)
        return res

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.ordereddict[key] = value
        self.ordereddict.move_to_end(key, last = False)
        if len(self.ordereddict) > self.capacity:
            self.ordereddict.popitem(last = True)
        return 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

