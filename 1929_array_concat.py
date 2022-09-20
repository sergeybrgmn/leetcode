"""
Problem to concat input array to the input array itself

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]

Link: https://leetcode.com/problems/concatenation-of-array/
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans.extend(ans)
        return ans


#Test cases:
solution = Solution()

#list of cases:
test_pairs = [
([1,2,1],[1,2,1,1,2,1]),
([1,3,2,1],[1,3,2,1,1,3,2,1])
]

for pair in test_pairs:
    output = solution.getConcatenation(pair[0])
    #print(output)
    assert output == pair[1]