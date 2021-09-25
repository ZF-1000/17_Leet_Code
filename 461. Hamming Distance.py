"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 231 - 1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        len_bin_x = len(bin_x)
        len_bin_y = len(bin_y)
        if len_bin_x > len_bin_y:
            bin_y = '0' * (len_bin_x - len_bin_y) + bin_y
        elif len_bin_x < len_bin_y:
            bin_x = '0' * (len_bin_y - len_bin_x) + bin_x
        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count


arr = [[1, 4], [3, 1]]

sol = Solution()
for el in arr:
    print(sol.hammingDistance(el[0], el[1]))
