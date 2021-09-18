"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str = ""
        for el in s:
            if el.isalpha() or el.isdigit():
                my_str += el
        my_str = my_str.lower()

        flag = True
        for i in range(len(my_str)):
            if my_str[i] == my_str[-i - 1]:
                flag = True
            else:
                flag = False
                break
        if flag:
            return True
        else:
            return False


# arr = ["0P"]
arr = ["A man, a plan, a canal: Panama", "race a car", "0P", "asdsa", "assa"]
sol = Solution()
for el in arr:
    print(sol.isPalindrome(el))
