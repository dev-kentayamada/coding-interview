#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# Reference: https://www.youtube.com/watch?v=ugBx_T1RHuc
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if (head == None):
            return None

        answerHead = Node(0, None, head, None)
        answer = answerHead

        stack = []

        while (head):
            if (head.child):
                child = head.child
                if (head.next):
                    stack.append(head.next)
                head.child = None
                answer.next = head
                head.prev = answer
                answer = answer.next
                head = child
            else:
                answer.next = head
                head.prev = answer
                answer = answer.next
                head = head.next

        while (stack):
            stacked_node = stack.pop()
            answer.next = stacked_node
            stacked_node.prev = answer

            # move pointer to the end of list
            while (answer.next):
                answer = answer.next

        # detach the pseudo head node from the result.
        answerHead.next.prev = None

        return answerHead.next


# @lc code=end
