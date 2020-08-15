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
    def hash_table(self, head):
        s = set()
        temp = head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False

    def two_pointers(self, head):
        slow = head
        fast = head.next.next

        while (slow != fast):
            if (fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return False
        #return self.hash_table(head)  # Time O(n) | Space O(n)
        return self.two_pointers(head) # Time O(n) | Space O(1)
# @lc code=end
