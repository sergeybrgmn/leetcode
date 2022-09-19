"""The class to calculate how many of the stones you have are also jewels. 
Strings <jewels> representing the types of stones that are jewels
String <stones> representing the stones you have

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
 
Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.

Link: https://leetcode.com/problems/jewels-and-stones/
"""
class Solution:         
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """The main func of the class"""    
        if (len(jewels) >= 1) and (len(stones) <= 50) and (stones.isalpha()):
            counter=0
            for stone in stones:
                if stone in jewels:
                    counter += 1
            return counter
        else:
            print("inputs are not within constrains")

#Test cases:

solution = Solution()

#list of cases:
test_pairs = [
("aA","aAAbbbb",3),
("z","ZZ",0),
("","ZZ",None)
]

for pair in test_pairs:
    output = solution.numJewelsInStones(jewels=pair[0],stones=pair[1])
    assert output == pair[2]
