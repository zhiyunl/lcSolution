"""
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
 A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.

Idea: regular dp algorithm
    bottom up computing a matrix of m x n, saving the length of LCS up to index m and n.
    if the [i] [j] elements are equal, increment by 1 from [i-1][j-1]
    else, we choose the biggest neighbour.
    return [m][n] as the length
    base case: padding a zero column and row to make sure i-1 and j-1 exists. assign 0 value.
corner case:
    text1 and/or text2 are null, return 0;

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if text1 is None or text2 is None:
        #     return 0
        lc = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        # lc = [[0] * (len(text2) + 1)] *(len(text1) + 1)
        for i, a in enumerate(text1):
            for j, b in enumerate(text2):
                if a == b:
                    lc[i + 1][j + 1] = lc[i][j] + 1
                else:
                    lc[i + 1][j + 1] = max(lc[i][j + 1], lc[i + 1][j])
        return lc[-1][-1]


if __name__ == '__main__':
    sl = Solution()
    t1 = "abcdedf"
    t2 = "abcdefddddddd"
    tmp = sl.longestCommonSubsequence(text1=t1, text2=t2)
    print(tmp)
