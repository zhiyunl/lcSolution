"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:
Could you solve it without converting the integer to a string?
Idea:
    1. negative numbers are false
    2. of course easiest way is str(int) and compare with reverse str, O(N) space
    3. int//10 removes last digits
    4. int%10 gets last digits
    5. revert and compare
    6. trick is only reverse half
Algorithm:
    1. if negative,ending with 0 but not 0, false
    2. while num not 0: "pop" last digits from num using modulo
            revert by x=10*x+pop
            **if x >= num, we reached the middle**
            if equal(even) or x//10==num (odd), True

edge case:
    1. None, return False
    2. negative,  False
    3. 0, True
    4. Overflowed: 2147483647, false
    5. ending with 0, false
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0 or x > 2147483647 or x % 10 == 0 and x is not 0:
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


sl = Solution()
test = [None, 0, -5, 1, 10, 121, 1221, 12321, 112321, 12345654321]
# last case is overflowed int, range [-2147483647,  2147483647]
for e in test:
    print("test case:" + str(e) + "\tresult:" + str(sl.isPalindrome(e)))
