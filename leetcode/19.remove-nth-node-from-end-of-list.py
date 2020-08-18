# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def two_pass(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        while (first):
            length += 1
            first = first.next

        pos = length - n

        first = dummy
        for _ in range(pos):
            first = first.next
        first.next = first.next.next
        return dummy.next

    def one_pass(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first, second = head, dummy

        for _ in range(n):
            first = first.next

        while (first):
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.two_pass(head, n)  # Time O(L) | Space O(1)
        # return self.one_pass(head, n)  # Time O(L) | Space O(1)
        # @lc code=end
