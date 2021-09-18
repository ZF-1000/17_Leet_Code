"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        a = "0" + a
        b = "0" + b
        target = ""
        flag = 0
        len_a = len(a)
        for i in range(-1, -len_a - 1, -1):
            if int(a[i]) + int(b[i]) + flag == 0:
                target += '0'
                flag = 0
            elif (int(a[i]) + int(b[i]) + flag) % 2 != 0:
                target += '1'
                flag = int((int(a[i]) + int(b[i]) + flag) / 2)
            elif (int(a[i]) + int(b[i]) + flag) % 2 == 0:
                target += '0'
                flag = (int(a[i]) + int(b[i]) + flag) / 2
        target = target[::-1]
        while target[0] == "0" and len(target) > 1:
            target = target[1:]
        return target


# arr = [["111", "1010"]]
arr = [["11", "1"], ["1010", "1011"], ["10", "1"], ["0", "1"], ["1", "0"], ["1", "1"], ["0", "0"], ["1111", "1111"],
       ["111", "1010"]]
sol = Solution()
for el in arr:
    print(sol.addBinary(el[0], el[1]))
