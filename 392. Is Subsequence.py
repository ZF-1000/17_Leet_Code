"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = False
        i = 0
        j = 0
        for i in range(len(s)):
            flag = False
            if j == len(t):
                flag = False
                break
            while j != len(t):
                if s[i] == t[j]:
                    flag = True
                    j += 1
                    break
                j += 1
        if i == len(s) - 1 and flag is True:
            return True
        elif len(s) == 0:
            return True
        else:
            return False


# arr = [["bb", "ahbgdc"]]
arr = [["abc", "ahbgdc"], ["axc", "ahbgdc"], ["ace", "abcde"], ["aec", "abcde"], ["", "ahbgdc"], ["bb", "ahbgdc"]]

sol = Solution()
for el in arr:
    print(sol.isSubsequence(el[0], el[1]))
