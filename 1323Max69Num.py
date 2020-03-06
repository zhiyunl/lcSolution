"""
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6)

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

Constraints:
    1 <= num <= 10^4
    num's digits are 6 or 9.
Idea:
    1. change the highest digits with value 6, linear scan. convert to string
    2. get digit by // and %
    3. python replace fucntion can find the first element in string and replace it, int(replace(str(num),'6','9'))
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        # num2str
        stri = list(str(num))
        for i, x in enumerate(stri):
            if x == '6':
                stri[i] = '9'
                break
        return int("".join(stri))
    # string slicing can be quicker, no need to convert to list


if __name__ == '__main__':
    sl = Solution()
    num = 996
    tmp = sl.maximum69Number(num)
    print(tmp)
