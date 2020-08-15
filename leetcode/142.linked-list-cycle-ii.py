#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        found = 0

        # floyd’s Cycle-Finding Algorithm
        while (fast and slow and fast.next):
            fast = fast.next.next
            slow = slow.next
            if (slow == fast):
                found = 1
                break

        if (found):  # if found cycle in the node
            fast = head  # or slow=head
            while (fast != slow):
                fast = fast.next
                slow = slow.next
            return fast
        return None
# @lc code=end
