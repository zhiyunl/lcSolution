"""
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

algorithm: 1. brute force uses O(n^2) time
    2. greedy, check if s[0]==s[-1], check s[1:-1] iteratively
                else check s[1:-1] and s[0:len-2] (only 1 deletion)
idea: 1. use head and tail pointers
        2. iteratively check
        3. if do recursively, need a flag to indicate deletion
        4. use global var to save space
edge cases: 1. s is None or empty, return True
"""


class Solution:
    stri = str
    delete = bool  # init will not working

    def isPalindrome(self, head: int, tail: int) -> bool:
        if tail <= head:
            return True
        elif self.stri[head] == self.stri[tail]:
            return self.isPalindrome(head + 1, tail - 1)
        else:
            if not self.delete:
                self.delete = True
                return self.isPalindrome(head, tail - 1) or self.isPalindrome(head + 1, tail)
            else:
                return False

    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        self.stri, self.delete = s, False
        return self.isPalindrome(0, len(s) - 1)

    # extremely slow and space consuming
    # improvement:
    #       1. an easier way to check palindrome is compare with reverse str[::-1]
    #       2. how about iterative approach
    #       3. reverse string to save space
    """
    note: assume s="acba" rev="abca" len=4
        init: head=0, tail=3
        1st:  0<3, a=a, head=1,tail=2
        2nd:  1<2, c!=b:
                judge s[1:2]==rev[2:3] or s[2:3]==rev[1:2]
        True
        
    """

    def validPalindrome2(self, s: str) -> bool:
        if not s:
            return True
        length = len(s)
        head, tail = 0, length - 1
        rev = s[::-1]
        while head < tail:
            if s[head] != s[tail]:
                return s[head:tail] == rev[length - tail:length - head] \
                       or s[head + 1:tail + 1] == rev[length - tail - 1:length - head - 1]
            head, tail = head + 1, tail - 1
        return True
    # time: faster than 85%


sl = Solution()
testcase = [None, "", "ac", "aba", "abc", "caba", "acba", "abca", "abac"]
for stri in testcase:
    print("test case:" + str(stri) + "\tresult:" + str(sl.validPalindrome2(stri)))
