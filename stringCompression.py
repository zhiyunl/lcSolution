"""
Given an array pf characters. compress it *in-place*
The length after compression must always be smaller than or equal to the original array
Every element of the array should be a character (not int) of length 1
After you are done modifying the input array in-place, return the new length of the array

Follow up: use O(1) extra space to solve it
input: array of characters,
output: length of new array
compress by counting consecutive characters and replace with char+count
e.g. ['a','a','a','a','a','b','b','b','b'] => ['a','5','b','4']
if 'a' doesn't repeat, don't compress,
Note:
    123 => 1,2,3
idea:
    1. use pointer to record current pos, traverse array
    2. another pointer to record insert pos,
    3. when finished, insert pos is length_new.
    4. use stack to extract digits in a number
    5. convert int to char using chr(int+48)
extreme case:
    1. ['a'] => ['a']
    2. [] => []
"""


class Solution:
    def compress(self, chars) -> int:
        cur = 0
        ins = 0
        lens = len(chars)
        while cur < lens:
            cnt = 1
            while cur < lens - 1 and chars[cur] == chars[cur + 1]:
                cur += 1
                cnt += 1
            if cnt == 1:
                # don't compress
                chars[ins] = chars[cur]
                ins += 1
            else:
                chars[ins] = chars[cur]
                ins += 1
                stack = []
                # extract
                while cnt > 0:
                    stack.append(chr(cnt % 10 + 48))
                    cnt = cnt // 10
                # write back FILO
                while stack:
                    chars[ins] = stack.pop()
                    ins += 1
            cur += 1  # point to next element
        return ins

# another easy way to do int to digits is, for digit in str(int):
#
