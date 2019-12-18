#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x<0]
        res = sign * int(str((abs(x)))[::-1])
        return res if -(2**31)-1 < res < (2**31) else 0

# @lc code=end
