#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(x) for x in digits]
        str1 = "".join(strings)
        num = int(str1)
        str1 = str(num+1)
        return [int(x) for x in str1]
# @lc code=end
