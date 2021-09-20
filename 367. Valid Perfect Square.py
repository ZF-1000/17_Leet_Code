"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        flag = True

        while flag:
            middle = int(left + (right - left) / 2)
            approx = middle * middle
            if approx > num:
                right = middle
            elif approx == num:
                # return middle
                return True
            elif right - left == 1:
                return False
            else:
                left = middle

            if abs(approx - num) > 0:
                flag = True


# arr = [101]
arr = [16, 14, 1, 4, 101, 2000105819]

sol = Solution()
for el in arr:
    print(sol.isPerfectSquare(el))
