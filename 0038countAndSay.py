"""
the count and say sequence of integers with the first five terms as following:
1. 1            read off as 11
2. 11           read off as 21
3. 21           read off as 1211
4. 1211         read off as 111221
5. 111221       read off as 312211
...
continuously generate sequence

input: given a integer n where 1<= n<=30, generate nth count and say sequence
extreme condition: input None, return None
                over 30 or less than 1, error
idea:
    1.fastest way would be save all this result and do lookup table, cost more space
    2.otherwise, have to generate sequentially, time cost O(i)
Note: first element is 1, no need to read it out.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n is None:
            return ""
        else:
            if n <= 1:
                return "1"
            else:
                str = "1"
                for j in range(n - 1):
                    cnt = 1
                    pre = str
                    str = ""
                    lens = len(pre)
                    i = 0
                    while (i < lens - 1):
                        if pre[i] == pre[i + 1]:
                            cnt += 1
                        else:
                            str += repr(cnt)
                            str += pre[i]
                            cnt = 1
                        i += 1
                    # process last element
                    str += repr(cnt)
                    str += pre[i]
            return str


import time

start = time.time()
sl = Solution()
print(sl.countAndSay(12))
print("time is %.5f" % ((time.time() - start) * 10000))

# can use lookup table for integer to str concatenation
# Cnt=[0,1,2,3,4,5,6,7,8,9] Cnt[cnt]
# this can be faster than repr.
# used many space, faster than 93%
