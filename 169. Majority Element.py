"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        arr = []
        for x in d.items():
            arr.append(x[1])
        max_val = max(arr)

        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k

        return get_key(d, max_val)


# nums = [[2, 2, 1, 1, 1, 2, 2]]
nums = [[3, 2, 3], [2, 2, 1, 1, 1, 2, 2]]
sol = Solution()
for el in nums:
    print(sol.majorityElement(el))
