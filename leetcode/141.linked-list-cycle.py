# @before-stub-for-debug-begin
from python3problem141 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def original(self, head):
        s = set()
        temp = head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False

    def floyd_cycle_detection(self, head):
        slow = head
        fast = head

        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True

    def hasCycle(self, head: ListNode) -> bool:
        # original = self.original(head)  # Time O(n) | Space O(n)
        # return original
        floyd_cycle_detection = self.floyd_cycle_detection(head) # Time O(n) | Space O(1)
        return floyd_cycle_detection
# @lc code=end
