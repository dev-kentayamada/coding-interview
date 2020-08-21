#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def twoPointer(self, head):
        vals = []
        temp = head
        while (temp):
            vals.append(temp.val)
            temp = temp.next
        return True if vals == vals[::-1] else False

    def isPalindrome(self, head: ListNode) -> bool:
        return self.twoPointer(head)  # Time O(n) | Space O(n)
# @lc code=end
