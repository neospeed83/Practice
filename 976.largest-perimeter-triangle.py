#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        for i in range(0,len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

# @lc code=end

