"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Idea:
1. traditionally, use stack, push when (, [, {, pop when ),],}.
2. if there is only '(' and ')', we can use a simple counting method
    map '(' to +1, and ')' to -1.
    linear scan counting, cnt should be non-negative along the way, zero when terminating.
3. extend to all types. use cnt[3] to monitor each type ( [ {
    consider "([)]", record the lru type, should be cleared first before clearing other type.
    recursion is needed, which is not efficient.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for i in s:
            if i in m:
                stack.append(m[i])
                # push the back one for comparing later
            else:
                if len(stack) == 0:
                    return False
                else:
                    elem = stack.pop()
                    if i != elem:
                        return False
                    else:
                        continue
        return len(stack) == 0

    def isBalancedSimple(self, s: str) -> bool:
        m = {
            '(': 1,
            ')': -1,
        }
        cnt = 0
        for i in s:
            cnt = cnt + m[i]
            if cnt < 0:
                return False
        return cnt == 0


teststr = "[(())]"
paraTest = "(((())))"
sol = Solution()
print(sol.isBalancedSimple(s=paraTest))
