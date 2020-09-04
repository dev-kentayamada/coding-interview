#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for a, b in zip(heights, sorted_heights):
            if a != b:
                count += 1
        return count
# @lc code=end
