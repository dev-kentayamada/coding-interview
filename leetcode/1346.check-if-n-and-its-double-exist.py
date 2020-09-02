#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i * 2 in arr:
                if i == 0 and arr.count(0) == 1:  # edge case when 0
                    pass
                else:
                    return True
        return False
# @lc code=end
