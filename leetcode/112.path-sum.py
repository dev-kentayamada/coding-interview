#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Reference: https://qiita.com/mhiro216/items/a2bff3f19a62f4d3015d
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        stack = [(root, root.val)]
        while stack:
            node, nodeVal = stack.pop()
            if node.right == None and node.left == None:
                if nodeVal == sum:
                    return True
            if node.right:
                stack.append((node.right, node.right.val + nodeVal))
            if node.left:
                stack.append((node.left, node.left.val + nodeVal))
        return False

# @lc code=end
