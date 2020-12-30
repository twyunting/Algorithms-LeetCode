#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)
        s = 0

        while l1 or l2 or s:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + s
            tail.next = ListNode(s % 10)
            tail = tail.next
            s = s // 10 # carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next 


        """
        #Solution 2
        carry = 0
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        
        if l1: # if l1 is existing
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
        
        if l2: # if l2 is existing
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
        
        if carry == 1:
            p.next = ListNode(1)

        return dummy.next
    """



        
# @lc code=end

