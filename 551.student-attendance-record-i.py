#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and s.count('LLL') == 0:
            return True
        return False
# @lc code=end

