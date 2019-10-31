"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
Definition: Alphanumeric includes A-Z a-z and 0-9.
ascii value:
        a: 97, z:122,
        0: 48, 9: 57,
        A: 65, Z: 90.
idea: comparision is not case sensitive, so convert to lowercase first by adding 32
    compare character with a and z, 0 and 9 to make sure it's a alphanumeric character.
    since its a string, 1. two pointers from head and tail, step towards center, compare each step.
            2. from center and spread out, not practical for this problem, as it contains dummy characters
            3. use stack to reverse and compare
extreme case:
        1. str is none, return True
        2. str len is 1, return True
"""


class Solution:
    def alphanumeric(self, ch: chr) -> bool:
        # check if it's alphanumeric character
        return 'a' <= ch <= 'z' or '0' <= ch <= '9'

    def isPalindrome1(self, s: str) -> bool:
        if not s:
            return True
        head = 0
        tail = len(s) - 1
        s = s.lower()
        while head < tail:
            if not self.alphanumeric(s[head]):
                head += 1
                continue
            if not self.alphanumeric(s[tail]):
                tail -= 1
                continue
            if s[head] != s[tail]:
                return False
            else:
                head += 1
                tail -= 1
        return True


# there is a builtin func isalnum(),


# def isPalindrome2(self, s: str) -> bool:
#     fo,bk=len(s)//2-1,(len(s)+1)//2
#     while fo >= 0 and bk <len(s):
#         if not s[fo].isalnum():
#             fo -= 1
#         elif not s[bk].isalnum():
#             bk += 1
#         elif s[fo].lower() != s[bk].lower():
#             return False
#         else:
#             bk += 1
#             fo -= 1
#     return True


sl = Solution()
stri = "A man, a plan, a canal: Panama"
# stri="abccdba"
print(sl.isPalindrome1(stri))
