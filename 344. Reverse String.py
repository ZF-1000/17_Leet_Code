"""
Write a function that reverses a string. The input string is given as an array of characters s.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.


Follow up: Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = -1
        while i < int(len(s) / 2):
            buf = s[j]
            s[j] = s[i]
            s[i] = buf
            j -= 1
            i += 1
        return s


arr = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"]]

sol = Solution()
for el in arr:
    print(sol.reverseString(el))
