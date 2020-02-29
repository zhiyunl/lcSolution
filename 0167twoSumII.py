"""
Given an array of integers that is already sorted in ascending order,
 find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such
that they add up to the target, where index1 must be less than index2.

Note:
    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution
    and you may not use the same element twice.
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Idea:
    1. Since sorted in ascending order, can use binary search, logn x n
    2. hash map get thing done in O(n)

Special: index starts from 1!!
Corner case:
    1. 1 element or empty: [-1,-1]
    2.
"""
from typing import List


class Solution:
    def binarySearch(self, list, head, tail, key):
        # head = 0
        # tail = len(list) - 1
        while head <= tail:
            mid = (tail + head) // 2
            if list[mid] == key:
                return mid
            elif list[mid] > key:
                tail = mid - 1
            else:
                head = mid + 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        for i, x in enumerate(numbers):
            # only search for later part, avoid overlapping
            index = self.binarySearch(numbers, i, len(numbers) - 1, target - x)
            if index == -1:
                continue
            elif index == i:
                # check left and right for same elements
                if numbers[index - 1] == x:
                    return [index, i + 1]
                elif numbers[index + 1] == x:
                    return [i + 1, index + 2]
            else:
                return [i + 1, index + 1]
        return [-1, -1]
    # the hash table sol is the same as 0001 twoSum, runs in O(n)


if __name__ == '__main__':
    sl = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    tmp = sl.twoSum(nums, target)
    print(tmp)
