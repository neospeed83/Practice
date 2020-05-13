#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = Counter(s)
        for i in range(0,len(s)):
            if dict[s[i]] == 1:
                return i
        return -1
# @lc code=end

