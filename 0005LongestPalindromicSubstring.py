"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
Idea:
    1. brute force, O(n^3)
    2. dp O(n^2) n^2 space
    3. extend O(n^2) O(n) space
    4. manacher's alg O(n)
    5. Suffix Tree
    6. Palindromic Tree
alg dp:
    1. use n^2 matrix to save bool value, indicates s[row:col] to be valid or not
    2. bottom up loop through substr length and start pos
    3. check dp[rwo+1,col-1] and head == tail
        len=2, special case, only check head==tail
    4. save best pairs along the way
extend:
    1. loop through center pos
    2. check even and odd palindrome around center, go longer as possible
    3. save best start,length pairs
Manacher's alg:
    1.
    #TODO
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        def isPalindrome(s1):
            l = len(s1)
            for i in range(l // 2):
                if s1[i] != s1[l - i - 1]:
                    return False
            return True

        # brute force
        cur = [0, 0]
        if len(s) == 0:
            return ""
        for k in range(1, len(s)):  # length of substring
            for i in range(len(s) - k):  # start pos
                if isPalindrome(s[i:i + k + 1]):
                    cur = [k, i]
                    break
        return s[cur[1]:cur[0] + cur[1] + 1]

    def longestPalindrome2(self, s: str) -> str:
        # dp
        # observe optimal string are constructed of sub-optimal string
        # use a matrix to save the true/false of substring,
        # i is start pos
        # j is stop pos
        n = len(s)
        if n <= 2:
            return s if s == s[::-1] else s[-1]
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True  # all 1 element str is palindrome
        cur = [0, 0]
        # bottom up
        # length = 2 is special, cannot expand by check head == tail
        length = 1
        for start in range(0, n - 1):
            # end = start+1
            if s[start] == s[start + 1]:
                dp[start][start + 1] = True
                cur = [start, start + 1]
        for length in range(1, n):
            for start in range(0, n - length):
                if dp[start + 1][start + length - 1] and s[start] == s[start + length]:
                    dp[start][start + length] = True
                    cur = [start, start + length]
        return s[cur[0]:cur[1] + 1]

    def longestPalindrome3(self, s: str) -> str:
        # extend
        if s == s[::-1]:
            return s
        n = len(s)
        if n <= 2:
            return s[0]
        k = 1
        cur = [0, 0]

        def checkLongest(left, right):
            nonlocal cur
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if right - left > cur[1]:
                        cur = [left, right - left]
                    left -= 1
                    right += 1
                else:
                    break

        # k is center pos
        while k < n:
            # expand even length
            checkLongest(k - 1, k)
            # expand odd length
            checkLongest(k - 1, k + 1)
            k += 1
        return s[cur[0]:cur[0] + cur[1] + 1]


if __name__ == '__main__':
    sl = Solution()
    s = \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    tmp = sl.longestPalindrome3(s)
    print(tmp)
