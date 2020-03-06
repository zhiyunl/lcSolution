"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100

Idea:
    1. brute force O(n^2)
    2. sort, then the res is   O(nlogn)
Algorithm2:
    1. sort in nlogn time, along with original index saved
    2. linear scan the sorted array, detect value change, set previous index before the change as the cnt
    3. during traversal, set res[saved index] as the cnt, duplicates are neglected because cnt is saved.
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, x in enumerate(nums):
            cnt = 0
            for y in nums:
                if y < x:
                    cnt += 1
            res[i] = cnt
        return res

    def smallerNumbersThanCurrent_Sort(self, nums: List[int]) -> List[int]:
        nums = sorted([[nums[i], i] for i in range(len(nums))])
        res = [0] * len(nums)
        x_pre = nums[0]
        cnt = 0
        for i, x in enumerate(nums):
            if x_pre[0] != x[0]:
                x_pre = x
                cnt = i
            res[x[1]] = cnt
        return res


if __name__ == '__main__':
    sl = Solution()
    nums = [8, 1, 2, 2, 3]
    nums1 = [7, 7, 7, 7, 7]
    tmp = sl.smallerNumbersThanCurrent_Sort(nums)
    print(tmp)
