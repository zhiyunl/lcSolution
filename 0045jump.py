"""
Jump Game II
Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Idea:
    1. # use bfs
        # set the range(0,nums[0]) as the first step range
        # then find in the range for maximum i+nums[i] value
        # update range, repeat until range includes last element
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # use bfs
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        sofar, level = 0, 0
        length = len(nums)-1
        while r < length:
            level += 1
            sofar = max([x+i for i,x in enumerate(nums[l+1:r+1])])+l+1
            if sofar >= length:
                return level+1
            l, r = r, sofar
        return level+1


if __name__ == '__main__':
    sl = Solution()
    nums = [2, 3, 1, 1, 4]
    num1 = [1]
    num2 = [1, 1, 2, 3, 4]
    num3 = []
    num4 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5]

    def test(nums):
        return sl.jump(nums)

    tmp = test(nums)
    print(test(num1))
    print(test(num2))
    print(test(num3))
    print(test(num4))

    print(tmp)
