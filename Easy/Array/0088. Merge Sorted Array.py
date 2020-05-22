class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Make a copt of nums1
        nums1_copy = nums1[:m]
        nums1[:] = []
        
        # Two get pointers for nums1_copy and nums2
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1
        
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        
        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
            
            
"""
Python支援列表切割（list slices），可以取得完整列表的一部分。支援切割操作的類型有str, bytes, list, tuple等。它的語法是...[left:right]或者...[left:right:stride]。假定nums變數的值是[1, 3, 5, 7, 8, 13, 20]，那麼下面幾個語句為真：
nums[2:5] == [5, 7, 8]從下標為2的元素切割到下標為5的元素，但不包含下標為5的元素。
nums[1:] == [3, 5, 7, 8, 13, 20]切割到最後一個元素。
nums[:-3] == [1, 3, 5, 7]從最開始的元素一直切割到倒數第3個元素。
nums[:] == [1, 3, 5, 7, 8, 13, 20]返回所有元素。改變新的列表不會影響到nums。
nums[1:5:2] == [3, 7]從下標為1的元素切割到下標為5的元素但不包含下標為5的元素，且步長為2
"""
                
        
