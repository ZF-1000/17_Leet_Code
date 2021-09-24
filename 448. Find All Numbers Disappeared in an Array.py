"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = []
        # if len(nums) == 1:
        #     return res
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         res.append(i)
        #     while i in nums:
        #         nums.remove(i)
        # return res

        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        res = []
        for i in range(1, len(nums) + 1):
            if i not in d:
                res.append(i)
        return res


# arr = []
arr = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1], [1, 1, 1], [1], [1, 2]]

sol = Solution()
for el in arr:
    print(sol.findDisappearedNumbers(el))
