"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        summ = 0
        max_summ = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                summ += nums[i]
            else:
                if summ > max_summ:
                    max_summ = summ
                    summ = 0
                else:
                    summ = 0
        if summ > max_summ:
            max_summ = summ
        return max_summ


arr = [[1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 0],
       [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

sol = Solution()
for el in arr:
    print(sol.findMaxConsecutiveOnes(el))
