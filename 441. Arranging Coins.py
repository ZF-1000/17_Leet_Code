"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where
the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



Example 1:
*
**
**_

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:
*
**
***
**__

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        res = 0
        if n == 1:
            return 1
        while i != n:
            res += i
            if n == res:
                return i
            elif n < res:
                return i - 1
            i += 1
        return i - 1


# arr = [2]
arr = [5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

sol = Solution()
for el in arr:
    print(sol.arrangeCoins(el))
