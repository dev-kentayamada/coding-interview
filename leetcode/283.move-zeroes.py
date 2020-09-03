#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if nums[i] == 0:
                j = i + 1
                while j != len(nums):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
                    else:
                        j += 1

# @lc code=end
