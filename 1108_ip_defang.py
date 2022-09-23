"""The module to process the format of IP address (make defanged). 

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

 Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Link: https://leetcode.com/problems/defanging-an-ip-address/

+ Regex use to validate IPv4 address format
Of course much faster to use ipaddress.ip_address("127.0.0.1")

"""

import re

class Solution:
    def defangIPaddr(self, address: str):
        if bool(re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", address)):
            return "Input OK", address.replace(".","[.]")  
        else:
            return "Input is not IPv4", None

#Test cases:

solution = Solution()

#list of cases:
test_pairs = [
("1.1.1.1","1[.]1[.]1[.]1"),
("255.100.50.0","255[.]100[.]50[.]0"),
("2.6.5000.o","2[.]6[.]5000[.]")
]

for pair in test_pairs:
    status, output = solution.defangIPaddr(address=pair[0])
    print(status)
    assert output == pair[1]
