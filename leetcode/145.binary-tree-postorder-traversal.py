#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
            node = stack.pop()
            if node is not None:
                answer.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return answer[::-1]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.iterations(root)
        # @lc code=end
