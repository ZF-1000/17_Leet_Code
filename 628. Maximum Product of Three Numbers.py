"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = []
        sort_nums = sorted(nums)
        max1 = sort_nums[-1] * sort_nums[-2] * sort_nums[-3]
        max2 = sort_nums[0] * sort_nums[1] * sort_nums[2]
        max3 = sort_nums[0] * sort_nums[1] * sort_nums[-1]
        max4 = sort_nums[0] * sort_nums[-1] * sort_nums[-2]
        max5 = sort_nums[-1] * sort_nums[0] * sort_nums[1]
        max6 = sort_nums[-1] * sort_nums[-2] * sort_nums[0]
        res.append(max1)
        res.append(max2)
        res.append(max3)
        res.append(max4)
        res.append(max5)
        res.append(max6)
        return max(res)


# arr = [[-1, -2, 1, 2, 3]]
arr = [
    [1, 2, 3],
    [1, 2, 3, 4],
    [-1, -2, -3],
    [-100, -98, -1, 2, 3, 4],
    [-1, -2, 1, 2, 3]
]

sol = Solution()
for el in arr:
    print(sol.maximumProduct(el))
