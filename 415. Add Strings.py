"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        else:
            num1 = "0" * (len(num2) - len(num1)) + num1
        num1 = "0" + num1
        num2 = "0" + num2
        target = ""
        flag = 0
        len_num1 = len(num1)
        for i in range(-1, -len_num1 - 1, -1):
            if int(num1[i]) + int(num2[i]) + flag == 0:
                target += '0'
                flag = 0
            elif (int(num1[i]) + int(num2[i]) + flag) % 10 != 0:
                target += str((int(num1[i]) + int(num2[i]) + flag) % 10)
                flag = int((int(num1[i]) + int(num2[i]) + flag) / 10)
            elif (int(num1[i]) + int(num2[i]) + flag) % 10 == 0:
                target += '0'
                flag = int((int(num1[i]) + int(num2[i]) + flag) / 10)
        target = target[::-1]
        while target[0] == "0" and len(target) > 1:
            target = target[1:]
        return target


# arr = [["1", "9"]]
arr = [["11", "123"], ["456", "77"], ["0", "0"], ["1", "9"]]

sol = Solution()
for el in arr:
    print(sol.addStrings(el[0], el[1]))
