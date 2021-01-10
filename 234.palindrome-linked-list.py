#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
        
        while slow:
            top = stack.pop()
            #print(top)
            #print(slow.val)
            if top != slow.val:
                return False
            slow = slow.next
        return True
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
"""
# @lc code=end

