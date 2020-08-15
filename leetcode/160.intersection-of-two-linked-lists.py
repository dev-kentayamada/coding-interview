#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def brute_force(self, headA, headB):
        pA = headA
        pB = headB

        # For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai
        while (pA):
            tempB = pB
            while (tempB):
                if (tempB == pA):
                    return pA
                tempB = tempB.next
            pA = pA.next
        return None

    def hash_table(self, headA, headB):
        pA = headA
        pB = headB
        s = set()

        # Traverse list A and store the address / reference to each node in a hash set
        while (pA):
            s.add(pA)
            pA = pA.next

        # check every node bi in list B: if bi appears in the hash set, then bi is the intersection node
        while (pB):
            if (pB in s):
                return pB
            pB = pB.next
        return None

    def two_pointers(self, headA, headB):
        pA = headA
        pB = headB

        # If at any point pA meets pB, then pA/pB is the intersection node.
        while (pA != pB):
            # When pA reaches the end of a list, then redirect it to the head of B
            pA = headB if pA == None else pA.next
            # when pB reaches the end of a list, redirect it the head of A.
            pB = headA if pB == None else pB.next
        return pA  # or pB

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None or headB == None):
            return None
        # return self.brute_force(headA, headB) # Time O(mn) | Space O(1)
        # return self.hash_table(headA, headB) # Time O(m+n) | Space O(m) or O(n)
        return self.two_pointers(headA, headB) # Time O(m+n) | Space O(1)
# @lc code=end
