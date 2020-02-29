"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

idea: top down with memoization(divide and conquer) or bottom up (dp), Kadane's alg
alg: divide and conquer
1. recursively call
2. check if it's saved value
3. if yes, return value
4. else compare value with 0, if greater,
kadane's alg:
1. scan array O(n)
2. sum elements up to this location, compare with new element, cur_sum=max
3. the best sum would be updated if the cur_sum is greater
4. iterate
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = float('-inf')  # set to 0 if want to return 0 when minus
        for i in nums:
            cur_sum = max(i, cur_sum + i)  # i -> 0
            best_sum = max(best_sum, cur_sum)
        return best_sum


sl = Solution()
str1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
str2 = [-1]
print(sl.maxSubArray(str1))
