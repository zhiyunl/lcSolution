"""
given a valid ipV4 address, return a defanged version of the IP address
A defanged IP address replaces every period "." with "[.]"

first, the ip addr provided is valid, no need to check validity,
second,find three dot and replace.
using stack would be good.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # stack = str()
        # faster without explicitly str()
        stack = ""
        for element in address:
            if element == '.':
                stack += "[.]"
            else:
                stack += element
        return stack


import time

N = 20
start = time.time()
for i in range(N):
    sl = Solution()
    # str = "192.168.1.1"
    str = "0.0.0.1"
    sl.defangIPaddr(str)

print("time is %.5f" % ((time.time() - start) * 10000 / N))
print(sl.defangIPaddr(str))
