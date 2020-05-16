#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]

        hr = combinations(hour, num)
        for x in list(hr):
            print(x)
        min = combinations(minute, num)


# @lc code=end
