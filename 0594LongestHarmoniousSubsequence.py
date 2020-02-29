"""
We define a harmounious array as an array where the difference between its maximum value
and its minimum value is exactly 1.Now, given an integer array, you need to find the length
 of its longest harmonious subsequence among all its possible subsequences.

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
Idea:
    1. do a linear scan and save map [key,count], sort the map with key,
    iterate over the map for a consecutive key pair with largest sum.
corner case:
    1. 1 element: 0
    2. empty list: 0
"""
from collections import defaultdict
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1  # this handles when dict[i] does not exist
        if len(dict) <= 1:
            return 0
        li = sorted(dict.keys())
        best = 0
        x_prev = li[0]

        for x in li[1:]:
            if x - x_prev == 1:
                best = max(best, dict[x] + dict[x_prev])
            x_prev = x
        return best


if __name__ == '__main__':
    sl = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
    tmp = sl.findLHS(nums=nums)
    print(tmp)
