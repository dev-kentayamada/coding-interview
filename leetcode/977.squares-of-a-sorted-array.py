#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)
# @lc code=end

