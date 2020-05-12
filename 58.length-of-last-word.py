#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        if len(s) == 0:
            return 0
        if s.find(" "):
            words = s.split()
            print("This is words",words)        
            if len(words) > 0:
                return len(words[-1])
            return 0
        else:
            return len(s)
# @lc code=end

