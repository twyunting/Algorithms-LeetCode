#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import math
        points.sort(key = lambda x: sqrt(x[0]**2 + x[1]**2)) # Euclidean distance formula
        # print points
        return points[:K]
        
# @lc code=end

