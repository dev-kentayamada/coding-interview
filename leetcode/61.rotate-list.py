#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        temp = head

        # get length of linked list
        length = 0
        while temp:
            length += 1
            prev = temp
            temp = temp.next

        # craete a cycle
        prev.next = head

        # if n > k
        if k > length:
            k = k % length

        num_rotate = length - k + 1

        for _ in range(num_rotate - 1):
            prev = head
            head = head.next
        prev.next = None

        return head


# @lc code=end
