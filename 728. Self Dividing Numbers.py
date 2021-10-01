"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].



Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]


Constraints:

1 <= left <= right <= 104
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def div_numb(numb):
            flag = True
            lst_numb = list(str(numb))
            for num in lst_numb:
                if int(num) != 0 and numb % int(num) == 0:
                    flag = True
                else:
                    flag = False
                    break
            if flag is True:
                return True
            else:
                return False

        res = []
        for el in range(left, right + 1):
            if div_numb(el) is True:
                res.append(el)
        return res


arr = [[1, 22], [47, 85]]

sol = Solution()
for el in arr:
    print(sol.selfDividingNumbers(el[0], el[1]))
