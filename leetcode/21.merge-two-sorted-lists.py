# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def iteration(self, l1, l2):
        answerHead = ListNode(0)
        answer = answerHead
        while (l1 and l2):
            if (l1.val <= l2.val):
                answer.next = l1
                l1 = l1.next
            else:
                answer.next = l2
                l2 = l2.next
            answer = answer.next
        answer.next = l1 if l1 != None else l2
        return answerHead.next

    # Reference: https://www.youtube.com/watch?v=bdWOmYL5d1g
    def recursion(self, l1, l2):
        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1
        elif (l1.val < l2.val):
            l1.next = self.recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.recursion(l1, l2.next)
            return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # return self.iteration(l1, l2)  # Time O(n+m) | Space O(1)
        return self.recursion(l1, l2)  # Time O(n+m) | Space O(n+m)

# @lc code=end
