#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nb = str(bin(n))
        if nb.count('00') == 0 and nb.count('11') == 0:
            return True
        return False
# @lc code=end
