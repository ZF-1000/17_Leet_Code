"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false


Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        string_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        string_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        flag = True
        for w in word:
            if w in string_uppercase:
                flag = True
            else:
                flag = False
                break
        if flag is True:
            return True

        for w in word:
            if w in string_lowercase:
                flag = True
            else:
                flag = False
                break
        if flag is True:
            return True

        for i in range(len(word)):
            if i == 0 and word[i] in string_uppercase:
                flag = True
            elif word[i] in string_lowercase:
                flag = True
            else:
                flag = False
                break
        if flag is True:
            return True
        else:
            return False


arr = ["USA", "leetcode", "Google", "FlaG", "AS"]

sol = Solution()
for el in arr:
    print(sol.detectCapitalUse(el))
