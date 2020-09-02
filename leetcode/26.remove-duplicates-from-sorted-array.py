#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def two_pointers(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

    def removeDuplicates(self, nums: List[int]) -> int:
        return self.two_pointers(nums)  # Time O(n) | Space O(1)


# @lc code=end
