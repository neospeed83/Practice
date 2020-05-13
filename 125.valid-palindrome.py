#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = ''.join(x for x in s if x.isalnum())
        s = s.lower()
        return True if s==s[::-1] else False
# @lc code=end

