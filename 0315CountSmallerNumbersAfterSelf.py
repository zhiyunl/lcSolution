"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Idea:
    1. brute force, O(n^2)
    2. sort, then
Algorithm:
    1. sort in O(nlogn)
    2.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        counts = [0] * length
        for i in range(length):
            j = i
            while j < length:
                if nums[i] > nums[j]:
                    counts[i] += 1
                j += 1
        return counts


# TODO TLE
if __name__ == '__main__':
    sl = Solution()
    nums = [5, 2, 6, 1]
    tmp = sl.countSmaller(nums)
    print(tmp)
