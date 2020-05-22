#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] < target:
                i+=1
            if numbers[i] + numbers[j] > target:
                j-=1
# @lc code=end
