#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        sorted_set_nums = sorted(set_nums, reverse=True)
        if len(sorted_set_nums) < 3:
            return max(sorted_set_nums)
        else:
            return sorted_set_nums[2]

# @lc code=end
