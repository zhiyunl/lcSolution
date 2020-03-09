"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
Idea:
    1. use a sliding window to detect 3-digit subarray
        if arr[2] is '#", falls in j to z and move right 3 step
        else parser arr[0] and move right 1 step
        * start from tail
corner:
    1. len <=2, falls in a-i
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 2
        res = ""
        while i < len(s):
            if s[i] == '#':
                res += chr(int(s[i - 2:i]) - 10 + ord('j'))
                i += 3
            else:
                res += chr(ord(s[i - 2]) - ord('1') + ord('a'))
                i += 1
        if len(s) >= 2:
            if s[-1] != '#':
                if s[-2] != '#':
                    res += chr(ord(s[-2]) - ord('1') + ord('a'))
                res += chr(ord(s[-1]) - ord('1') + ord('a'))
        else:
            res += chr(ord(s[-1]) - ord('1') + ord('a'))
        return res


if __name__ == '__main__':
    sl = Solution()
    nums = "123456789"
    nums1 = "1"
    tmp = sl.freqAlphabets(nums1)
    print(tmp)
