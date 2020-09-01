#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Reference: https://www.youtube.com/watch?v=OvpKeraoxW0


class Solution:

    def iterative(self, head):
        if (head == None):
            return None

        temp = head

        # Creating a new weaved list of original and copied nodes.
        while (temp):
            new_node = Node(temp.val, None, None)
            nextNode = temp.next
            temp.next = new_node
            new_node.next = nextNode
            temp = temp.next.next

        # map "random" pointer
        temp = head
        while (temp):
            temp.next.random = temp.random.next if temp.random else None  # case of NULL
            temp = temp.next.next

        # Unweave the linked list to get back the original linked list and the cloned list
        temp = head
        while (temp):
            if (temp.next.next == None):
                break
            savedNode = temp.next.next
            temp.next.next = savedNode.next
            temp = savedNode
        return head.next

    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.iterative(head)  # Time O(n) | Space O(1)

# @lc code=end
