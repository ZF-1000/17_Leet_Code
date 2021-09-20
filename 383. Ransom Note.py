"""
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and
false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_list = list(ransomNote)
        magazine_list = list(magazine)
        for el in ransomNote_list:
            j = 0
            while j < len(magazine_list):
                if el == magazine_list[j]:
                    magazine_list[j] = '_'
                    break
                elif j == len(magazine_list) - 1:
                    return False
                j += 1
        return True


# arr = [["aab", "baa"]]
arr = [["a", "b"], ["aa", "ab"], ["aa", "aab"], ["aab", "baa"]]

sol = Solution()
for el in arr:
    print(sol.canConstruct(el[0], el[1]))
