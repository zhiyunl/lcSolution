"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Note:

    S.length <= 10000
    S[i] is "(" or ")"
    S is a valid parentheses string
Idea:
    1. first, identify the primitive parentheses, using counting method
    2. remove leftest and rightest
    2. concatenate and output
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        Dict = {'(': +1, ')': -1}
        cnt = 0
        head = 0
        res = ""
        for tail in range(len(S)):
            cnt += Dict[S[tail]]

            if cnt == 0:
                res+=S[head + 1:tail]
                head = tail + 1
        return res


if __name__ == '__main__':
    sl = Solution()
    nums = "(()())(())(()(()))"
    nums1= "()()"
    tmp = sl.removeOuterParentheses(nums)
    print(tmp)
