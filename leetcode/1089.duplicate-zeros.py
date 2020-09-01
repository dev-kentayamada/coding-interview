#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        length_arr = len(arr)

        while i < length_arr:
            if i == length_arr - 1 and arr[i] == 0: #if "0" at the end of the list
                break
            if arr[i] == 0:
                save = arr[i + 1:length_arr]
                arr[i + 1] = 0
                save = save[:-1]
                arr[i + 2:length_arr] = save
                i += 2
            else:
                i += 1
# @lc code=end
