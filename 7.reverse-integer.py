#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        result = []
        if x == "-":
            result[0] = "-"
            result.append(x[1:]) 
        else:
            result = x[::-1]
        
        while result[0] == 0:
            result.remove[0]
        
        return int(result)


# @lc code=end
