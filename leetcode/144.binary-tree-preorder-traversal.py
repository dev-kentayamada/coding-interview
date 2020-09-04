#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterations(self, root):
        if root is None:
            return []
        stack, answer = [root], []
        while stack:
            root = stack.pop()
            if root is not None:
                answer.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return answer

    # Reference: https://mingwho.com/posts/morris-traversal/
    def morrisTraversal(self, root):
        node, answer = root, []
        while node:
            if node.left is None:
                answer.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right != None and predecessor.right != node:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    answer.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return answer

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.iterations(root)  # Time O(n) | Space O(n)
        return self.morrisTraversal(root)  # Time O(n) | Space O(n)
# @lc code=end
