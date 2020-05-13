#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Play with Chips
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:      
        
        # Because ith chip is at index i 
        # all odd no cost 1 even no cost nothing.
        # so if we find evens and odds
        # and return the lowest of two.
        
        even = 0
        odd = 0
        for no in chips:
            if no % 2 == 0:
                even+=1
            else:
                odd+=1
        return even if even<odd else odd     
# @lc code=end

