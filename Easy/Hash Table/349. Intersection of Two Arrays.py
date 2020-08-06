# Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return Counter(nums1) & Counter(nums2)
        

# set

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return nums1 & nums2
    
# set without "&"

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        res = []
        
        if len(set1) < len(set2):
            for i in set1:
                if i in set2:
                    res.append(i)
        else:
            for i in set2:
                if i in set1:
                    res.append(i)
        return res
    
