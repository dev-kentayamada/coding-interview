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
    def hash_table(self, head):
        visited = set()
        temp = head
        while (temp):
            if (temp in visited):
                return temp
            visited.add(temp)
            temp = temp.next
        return None

    def floyd_cycle_algorithm(self, head):
        fast = head
        slow = head
        found = 0

        while (fast and slow and fast.next):
            fast = fast.next.next
            slow = slow.next
            if (slow == fast):
                found = 1
                break

        if (found):  # if found cycle in the node
            fast = head  # or slow = head
            while (fast != slow):
                fast = fast.next
                slow = slow.next
            return fast
        return None
    def detectCycle(self, head: ListNode) -> ListNode:
        return self.hash_table(head) # Time O(n) | Space O(n)
        #return self.floyd_cycle_algorithm(head) # Time O(n) | Space O(1)
# @lc code=end
