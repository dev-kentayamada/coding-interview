#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if (head == None):
            return None

        dummy = ListNode(0)
        dummy.next = head
        dummy_p = dummy

        while (dummy_p.next):
            if (dummy_p.next.val == val):
                dummy_p.next = dummy_p.next.next
            else:
                dummy_p = dummy_p.next
        return dummy.next
# @lc code=end
