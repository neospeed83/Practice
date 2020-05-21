#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

# @lc code=end

