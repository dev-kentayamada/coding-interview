#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (head == None):
            return None

        oddHead = ListNode(0)
        evenHead = ListNode(0)

        odd_p, even_p = oddHead, evenHead

        while (head):
            odd_p.next = head
            odd_p = odd_p.next
            even_p.next = head.next
            even_p = even_p.next

            if (head.next == None):
                break
            head = head.next.next

        odd_p.next = evenHead.next

        return oddHead.next


# @lc code=end
