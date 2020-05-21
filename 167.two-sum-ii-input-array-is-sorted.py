#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            if numbers[i] <= target:
                for j in range(i+1,len(numbers)):    
                    if numbers[j] <= target:
                        if numbers[i] + numbers[j] == target:       
                            return [i+1,j+1]
# @lc code=end
