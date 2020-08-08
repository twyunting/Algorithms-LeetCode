# & and elements()

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return (c1 & c2).elements()
        
