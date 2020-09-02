#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 0
        while i + 1 < len(A) and A[i] < A[i + 1]:
            i += 1

        # edge case : [0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0]
        if i == len(A) - 1 or i == 0:
            return False

        while i + 1 < len(A) and A[i] > A[i + 1]:
            i += 1
        if i == len(A) - 1:
            return True
        else:
            return False
        # @lc code=end
