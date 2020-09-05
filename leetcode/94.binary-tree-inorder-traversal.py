#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, answer = [], []
        while root != None or len(stack) != 0:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                answer.append(root.val)
                root = root.right
        return answer
# @lc code=end

