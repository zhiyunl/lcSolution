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


teststr = "[(())]"
sol = Solution()
print(sol.isValid(s=teststr))
