"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums = list(set_nums)
        if len(nums) == 2 or len(nums) == 1:
            return max(nums)
        for i in range(3):
            max_num = max(nums)
            index_max_num = nums.index(max_num)
            third_max_num = nums.pop(index_max_num)
            if len(nums) != 0 and third_max_num == max(nums):
                index_max_num = nums.index(max(nums))
                third_max_num = nums.pop(index_max_num)
                return third_max_num
        return third_max_num


# arr = [[1, 1, 2]]
arr = [[3, 2, 1], [1, 2], [2, 2, 3, 1], [1], [1, 1, 2]]

sol = Solution()
for el in arr:
    print(sol.thirdMax(el))
