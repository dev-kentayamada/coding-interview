#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
# @lc code=end
