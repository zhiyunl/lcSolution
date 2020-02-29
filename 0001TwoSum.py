"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.You may assume that each input would have
exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
return [0, 1].

Idea:
    use an extra array dif for difference between nums and target,
    brute force:  for every element in dif: search in nums. n^2
    binary search: sort array in nlogn time, binary search for logn x n.  nlogn
    hashTable(Dict): save index with key, finding a element in hash table is O(1), total O(n)
Special case:
    check when nums = target/2, make sure they are not the same indices.
corner case:
    1. empty or 1 element: N/A
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        dif = [target - x for x in nums]
        for i, x in enumerate(dif):
            for j, y in enumerate(nums):
                if x == y and i != j:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # binary search
        # nums = [[nums[i],i] for i in range(len(nums))]
        # nums.sort(key=lambda x:(x[0]))
        tmp = nums[:]
        nums.sort()
        for i, x in enumerate(nums):
            # search target-i in nums
            dif = target - x
            head = 0
            tail = len(nums)
            while head <= tail:
                mid = (head + tail) // 2
                if dif == nums[mid]:  # repeated numbers
                    if i != mid:
                        pass  # return [i, mid]
                    elif dif == nums[mid + 1]:
                        mid = mid + 1
                        # return [i, mid + 1]
                    elif dif == nums[mid - 1]:
                        mid = mid - 1
                        # return [i, mid - 1]
                    else:
                        return [-1, -1]
                    # search for index
                    for j, p in enumerate(tmp):
                        if p == x:
                            i = j
                            continue
                        if p == dif:
                            mid = j
                            continue
                    return [i, mid]
                elif dif > nums[mid]:
                    head = mid + 1
                else:
                    tail = mid - 1
            return [-1, -1]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        # hash table, check and look back, avoiding same key value error
        dict = {}
        for i, x in enumerate(nums):
            if target - x in dict.keys() and dict[target - x] != i:
                return [dict[target - x], i]
            dict[x] = i
        return [-1, -1]


if __name__ == '__main__':
    sl = Solution()
    nums = [9, 8, 7, 6, 3, 5, 5]
    target = 10
    tmp = sl.twoSum3(nums, target)
    print(tmp)
