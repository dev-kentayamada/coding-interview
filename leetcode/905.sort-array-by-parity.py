#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = 0
        for _ in range(len(A)):
            if A[j] % 2 != 0:
                temp = A[j]
                A.pop(j)
                A.append(temp)
            else:
                j += 1
        return A
# @lc code=end

