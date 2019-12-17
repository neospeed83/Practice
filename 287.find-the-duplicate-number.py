#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        test = nums[:]
        test.sort()
        for i in range(1,len(test)):
            if test[i] == test[i - 1]:
                return test[i]

# @lc code=end

