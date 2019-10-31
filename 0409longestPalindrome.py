"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is *case sensitive*, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Idea:
    1. find #pairs, longest is #pairs x 2, possible plus 1 in the middle, such as "abcba"
    2. O(N) time. O(1) space
Algorithm:
    1. keep a table of characters, use dictionary average O(1) worst O(N)
    2. traverse str, update dict
    3. count pairs in dict, calculate length
edge case:
    1. None or empty, 0
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        table = {}
        length = 0
        res = 0
        for e in s:
            table[e] = 1 + table[e] if e in table.keys() else 1
        for val in table.values():
            length += val // 2
            if val % 2:
                res = 1
        return length * 2 + res


"""
Amazing solution found on leetcode forum author:https://leetcode.com/stefanpochmann/
def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
    
def longestPalindrome(self, s):
    use = sum(v & ~1 for v in collections.Counter(s).values())
    return use + (use < len(s))

def longestPalindrome(self, s):
    counts = collections.Counter(s).values()
    return sum(v & ~1 for v in counts) + any(v & 1 for v in counts)
"""

sl = Solution()
test = [None, "", "a", "ac", "aba", "abc", "aaa", "aaac", "aaaac"]
for e in test:
    print("test case:" + str(e) + "\tresult:" + str(sl.longestPalindrome(e)))
