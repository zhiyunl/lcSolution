"""
write a function to find the longest common prefix string amongst an array of strings.
input: [str1, str2, str3 ....], strings are *all* lowercase a-z
output: string
extreme case: If no common prefix return ""
        if empty array/ None, return ""
        if empty string, return ""

note: *common to all*
first, find minimum length
traverse through all array, compare first element
second,continue to minimum length of elements
Until null/diff
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs is None or strs == []:
            return ""
        common = ""
        minlen = len(strs[0])
        #  get min length
        arr_len = len(strs)
        for i in range(arr_len):
            if strs[i] is None or strs[i] == "":
                return ""
            else:
                minlen = min(minlen, len(strs[i]))

        for i in range(minlen):
            for j in range(1, arr_len):
                if strs[j][i] != strs[0][i]:
                    return common
            common += strs[0][i]
        return common


import time

N = 20
start = time.time()
sl = Solution()
list = ["flower", "flow", "flight"]
# list = ["dog", "racecar", "car"]
for i in range(N):
    sl.longestCommonPrefix(list)
print("time is %.5f" % ((time.time() - start) * 10000 / N))
print(sl.longestCommonPrefix(list))

# can use devide and conquer
# can use binary search
# use sorted can improve efficiency
