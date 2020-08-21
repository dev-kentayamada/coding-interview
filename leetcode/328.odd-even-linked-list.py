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

        # traverse linked list
        while (head):
            # create an odd nodes linked list
            odd_p.next = head
            odd_p = odd_p.next
            # create an even nodes linked list
            even_p.next = head.next
            even_p = even_p.next

            # check if there is node
            if (head.next == None):
                break
            else:
                head = head.next.next

        # concat odd node linked list and even node linked list
        odd_p.next = evenHead.next

        return oddHead.next


# @lc code=end
