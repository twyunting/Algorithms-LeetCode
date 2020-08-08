# & and elements()

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return (c1 & c2).elements()
        
# dictionary

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1, res = {}, []
        for i in nums1:
            c1[i] = c1.get(i, 0) +1 # same method with Counter(nums1)
    
        for i in nums2:
            if i in c1 and c1[i] > 0:
                res.append(i)
                c1[i] -= 1
        return res
    
# two pointer (must use sort)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        p1, p2, res = 0, 0, []
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
        return res

# Counter
    
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        
        for i in c1:
            if i in c2:
                res += [i] * min(c1[i], c2[i])
        return res
    
    
    
