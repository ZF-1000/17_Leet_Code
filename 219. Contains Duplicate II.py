"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def dubl_list(nums):
            d = {}
            for num in nums:
                if num not in d:
                    d[num] = 0
                d[num] += 1
            # d: {1: 2, 2: 1, 3: 1}
            dubl = []
            for x in d.items():
                if x[1] > 1:
                    dubl.append(x[0])
            return dubl

        dubl = dubl_list(nums)
        for d in dubl:
            lst_index = []
            for i in range(len(nums)):
                if nums[i] == d:
                    lst_index.append(i)
            for j in range((len(lst_index)) - 1):
                for n in range(1, len(lst_index)):
                    if j != n and abs(lst_index[j] - lst_index[n]) <= k:
                        return True
        return False


# nums = [[[1, 0, 1, 1], 1], ]
nums = [[[1, 2, 3, 1], 3], [[1, 0, 1, 1], 1], [[1, 2, 3, 1, 2, 3], 2]]
sol = Solution()
for el in nums:
    print(sol.containsNearbyDuplicate(el[0], el[1]))
