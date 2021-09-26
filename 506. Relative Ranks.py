"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score,
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number
(i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.



Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].



Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [0 for _ in range(len(score))]
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        for i in range(3):
            max_el = max(score)
            ind_el = score.index(max_el)
            score[ind_el] = -1
            res[ind_el] = medals[i]
            if i == len(score) - 1:
                return res

        for j in range(3, len(score)):
            max_el = max(score)
            ind_el = score.index(max_el)
            score[ind_el] = -1
            res[ind_el] = str(j + 1)
        return res


arr = [[123123, 11921, 1, 0, 123]]
# arr = [[5, 4, 3, 2, 1], [10, 3, 8, 9, 4], [12, 13, 2, 4, 3], [1], [4, 2], [3, 4, 1]]

sol = Solution()
for el in arr:
    print(sol.findRelativeRanks(el))
