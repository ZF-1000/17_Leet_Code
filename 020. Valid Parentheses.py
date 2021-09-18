"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        len_s = 1
        len_s1 = 2
        while len_s != len_s1:
            len_s = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            len_s1 = len(s)
        if not s:
            return (True)
        else:
            return (False)


sol = Solution()
arr_s = ["()", "()[]{}", "(]", "([)]", "{[]}"]
for s in arr_s:
    print(sol.isValid(s))
