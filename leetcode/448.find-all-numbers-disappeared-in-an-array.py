#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def hashMap(self, nums):
        answer = []
        hashTable = {}

        for num in nums:
            hashTable[num] = 1

        for i in range(1, len(nums) + 1):
            if i not in hashTable:
                answer.append(i)
        return answer

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return self.hashMap(nums)  # Time O(n) | Space O(n)

# @lc code=end
