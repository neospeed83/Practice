#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        
        def getVal(c):
            if c == 'I':
                return 1
            if c == 'V':
                return 5
            if c == 'X':
                return 10
            if c == 'L':
                return 50
            if c == 'C':
                return 100
            if c == 'D':
                return 500
            if c == 'M':
                return 1000
            
        res = 0
        for i in range(0, len(s)):
            if s[i] == 'I' and s[i+1] in {'V','X'}:
                pass
            elif s[i] == 'X' and s[i+1] in {'L','C'}:
                pass
            elif s[i] == 'C' and s[i+1] in {'D','M'}:
                pass
            else:
                res += getVal(s[i])
                




# @lc code=end

