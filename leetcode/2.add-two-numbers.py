# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answerHead = ListNode(0)
        answer = answerHead
        temp = 0
        while (l1 or l2 or temp > 0):
            if (l1 != None):
                temp += l1.val
                l1 = l1.next
            if (l2 != None):
                temp += l2.val
                l2 = l2.next
            answer.next = ListNode(temp % 10)
            answer = answer.next
            temp = temp // 10
        return answerHead.next
# @lc code=end
