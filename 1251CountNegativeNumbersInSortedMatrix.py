"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
Idea:
    1. binary search 0 row wise and column wise
    2. brute force, O(mn)
    3. boundary O(m+n)
Algorithm3: count the positive first
    1. start from left-bottom, since its non-decreasing, when x >=0, all elements in this column is positive, +row, go right
    2. else, go up, thus, going along the boundary of negative and positive.
    3. until reach the right top.
    like city-block distance, O(m+n)
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # brute force
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    break
                cnt += 1
        return len(grid) * len(grid[0]) - cnt

    def countNegatives3(self, grid: List[List[int]]) -> int:
        # boundary
        cnt = 0
        row, col = len(grid) - 1, 0
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] >= 0:
                cnt += row + 1
                col += 1
            else:
                row -= 1
        return len(grid) * len(grid[0]) - cnt


if __name__ == '__main__':
    sl = Solution()
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    tmp = sl.countNegatives3(grid)
    print(tmp)
