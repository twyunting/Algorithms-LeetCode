#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # create dummy head
        dummy_head = ListNode(0)
        dummy_head.next = head

        # identify the length
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        # identify the location to be removed
        node = dummy_head
        for _ in range(length-n):
            node = node.next
        
        # perform removal
        previous = node
        following = node.next.next
        previous.next = following

        return dummy_head.next

            


# @lc code=end

