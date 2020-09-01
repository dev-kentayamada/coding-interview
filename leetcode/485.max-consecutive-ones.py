#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count, max_count)  # Time O(n) | Space O(1)

# @lc code=end
