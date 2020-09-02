#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def two_pointers(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[j] = nums[i]
                j += 1
        return j
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.two_pointers(nums, val)  # Time O(n) | Space O(1)
# @lc code=end
