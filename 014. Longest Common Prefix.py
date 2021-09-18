"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []

        for i in strs:
            arr.append(len(i))
        min_el = min(arr)

        common_pref = ''
        flag = True
        for i in range(min_el):
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                common_pref += strs[0][i]
            else:
                break
        return (common_pref)


sol = Solution()
strs = ["flower", "flow", "flight"]
strs1 = ["dog", "racecar", "car"]
strs2 = ["ab", "a"]

print(sol.longestCommonPrefix(strs))
print(sol.longestCommonPrefix(strs1))
print(sol.longestCommonPrefix(strs2))
