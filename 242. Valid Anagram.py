"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_t = list(t)

        flag = False
        for i in range(len(s)):
            flag = False
            j = 0
            while j < len(str_t):
                if s[i] == str_t[j]:
                    str_t.remove(str_t[j])
                    flag = True
                    break
                else:
                    j += 1
        if len(str_t) == 0 and flag is True:
            return True
        else:
            return False


# arr = [["ab", "a"]]
arr = [["anagram", "nagaram"], ["rat", "car"], ["ab", "a"]]

sol = Solution()
for el in arr:
    print(sol.isAnagram(el[0], el[1]))
