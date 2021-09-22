"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1


Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int) -> int:
        sum_num = num
        list_num = list(str(num))
        while len(list_num) > 1:
            sum_num = 0
            for i in list_num:
                sum_num += int(i)
            list_num = list(str(sum_num))
        return sum_num


# arr = [1]
arr = [38, 0, 98756325, 1]

sol = Solution()
for el in arr:
    print(sol.addDigits(el))
