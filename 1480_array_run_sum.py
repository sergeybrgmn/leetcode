"""

sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


LINK https://leetcode.com/problems/running-sum-of-1d-array/

"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum=0
        for num in nums:
            sum += num
            output.append(sum)
        return output


#Test cases:

solution = Solution()

#list of cases:
test_pairs = [
([1,2,3,4],[1,3,6,10]),
([1,1,1,1,1],[1,2,3,4,5]),
([3,1,2,10,1],[3,4,6,16,17])
]

for pair in test_pairs:
    output = solution.runningSum(nums=pair[0])
    assert output == pair[1]
