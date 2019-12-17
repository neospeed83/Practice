#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(heights):
            if max < heights[i]:
                max = i


# @lc code=end

