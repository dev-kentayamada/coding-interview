#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        stack = [root.left, root.right]
        while any(stack):  # e.g. [None, None, None, None]
            nodeLeft = stack.pop(0)
            nodeRight = stack.pop(0)
            if nodeLeft == None and nodeRight:
                return False
            elif nodeLeft and nodeRight == None:
                return False
            elif nodeLeft and nodeRight:
                if nodeLeft.val != nodeRight.val:
                    return False
            if nodeLeft:
                stack.append(nodeLeft.left)
            if nodeRight:
                stack.append(nodeRight.right)
            if nodeLeft:
                stack.append(nodeLeft.right)
            if nodeRight:
                stack.append(nodeRight.left)
        return True
# @lc code=end
