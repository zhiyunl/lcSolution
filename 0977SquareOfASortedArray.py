"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number,
also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

Idea:
    1. find center and use two pointers, do merge

"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [x * x for x in A]
        # find the flip point near 0
        cur = len(A) - 1
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                cur = i
                break
        forward = cur - 1
        backward = cur + 1
        res = [A[cur]]
        while forward >= 0 and backward < len(A):
            if A[forward] < A[backward]:
                res.append(A[forward])
                forward -= 1
            else:
                res.append(A[backward])
                backward += 1
        if forward >= 0:
            res += A[forward::-1]
        elif backward < len(A):
            res += A[backward:]
        return res


if __name__ == '__main__':
    sl = Solution()
    nums = [-4, -1, 0, 3, 10]
    nums1 = [-1,1]
    tmp = sl.sortedSquares(nums1)
    print(tmp)
