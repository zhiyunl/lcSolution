"""
Given an array arr, replace every element in that array
with the greatest element among the elements to its right,
and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
Idea:
    1. start from end, keep maximum value, in-place, Time O(n)
corner:
    1. 1 element, [-1]
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]
        for i in range(len(arr) - 1, -1, -1): # not inclusive
            maxi = max(arr[i], maxi)
            arr[i] = maxi
        return arr[1:]+[-1]


if __name__ == '__main__':
    sl = Solution()
    nums = [17,18,5,4,6,1]
    nums1 = [7]
    tmp = sl.replaceElements(nums1)
    print(tmp)
