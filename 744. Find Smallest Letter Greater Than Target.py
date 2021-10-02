"""
Given a characters array letters that is sorted in non-decreasing order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = list(set(letters))
        string_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        lst_str = list(string_lowercase)
        i = 0
        while i < 26:
            if target == lst_str[i]:
                j = i + 1
                if j == 26:
                    j = 0
                while j < 26:
                    if lst_str[j] in letters:
                        return lst_str[j]
                    j += 1
                    if j == 25 or j == 26:
                        j = 0
            i += 1
            if i == 26:
                i = 0


arr = [
    [["c", "f", "j"], "a"],
    [["c", "f", "j"], "c"],
    [["c", "f", "j"], "d"],
    [["c", "f", "j"], "g"],
    [["c", "f", "j"], "j"],
    [["a", "b"], "z"],
    [["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "y"]
]

sol = Solution()
for el in arr:
    print(sol.nextGreatestLetter(el[0], el[1]))
