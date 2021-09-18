"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = x
        num = 0
        if x > 0:
            while x > 0:
                num = num * 10 + (x % 10)
                x = x // 10
            if x1 == num:
                return (True)
            else:
                return (False)
        elif x == 0:
            return (True)
        else:
            return (False)


s = Solution()
arr = [121, -121, 10, -101, 0]
for x in arr:
    print(s.isPalindrome(x))
