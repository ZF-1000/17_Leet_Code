"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            str_num = str(x)
            str_num = str_num[:0:-1]
            int_num = int(str_num)
            if int_num <= 2147483648:
                return (-(int_num))
            else:
                return (0)
        elif x > 0:
            str_num = str(x)
            str_num = str_num[::-1].lstrip('0')
            int_num = int(str_num)
            if int_num <= 2147483647:
                return (int_num)
            else:
                return (0)
        else:
            return (0)


s = Solution()
arr = [123, -123, 120, 0, 1534236469]
for x in arr:
    print(s.reverse(x))
