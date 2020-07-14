# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Answer:
    def OnePass_HashTable(nums,target):
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return (hash_table[target - num], i)
            hash_table[num] = i
        return []
    def TwoPass_HashTable(nums, target):
        hash_table = dict()
        for i, num in enumerate(nums):
            hash_table[num] = i
        for i, num in enumerate(nums):
            if target - num in hash_table:
                if (hash_table[target - num] != i):
                    return (hash_table[target - num], i)
        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if (nums[i] + nums[k] == target):
                    return [i, k]
        #return Answer.OnePass_HashTable(nums, target)
        #return Answer.TwoPass_HashTable(nums, target)
# @lc code=end

