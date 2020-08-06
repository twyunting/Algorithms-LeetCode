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
    
# two pointer

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=set()
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                ans.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return list(ans)
    
    
