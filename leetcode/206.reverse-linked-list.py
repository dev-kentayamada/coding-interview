# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def iterative(self, head):
        prev = None
        cur = head
        while (cur):
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev

    # Reference: https://www.youtube.com/watch?v=Ip4y7Inx7QY
    def recursive(self, head):
        cur = head
        if (cur == None):  # e.g.[]
            return None
        elif (cur.next == None):  # e.g.[5]
            return cur
        else:
            nextNode = cur.next
            cur.next = None
            rest = self.recursive(nextNode)
            nextNode.next = cur
            return rest

    def reverseList(self, head: ListNode) -> ListNode:
        # return self.iterative(head)  # Time O(n) | Space O(1)
        return self.recursive(head)  # Time O(n) | Space O(1)

# @lc code=end
