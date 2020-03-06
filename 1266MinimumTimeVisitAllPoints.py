"""
On a plane there are n points with integer coordinates points[i] = [xi, yi].
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:
    In one second always you can either move vertically, horizontally by one unit or diagonally
    (it means to move one unit vertically and one unit horizontally in one second).
    You have to visit the points in the same order as they appear in the array.
Idea:
    1. Greedy, first we move diagonally, until vertical/ horizontal axis are the same, then just add up the diff.
        diff x>y, then time = x-y +x-(x-y) = x. So, time = max(diff x,y)
corner:
    1. 1 point/ empty, return 0
"""
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        length = len(points)
        if length <= 1:
            return 0
        for i in range(length - 1):
            x_delta = abs(points[i + 1][0] - points[i][0])
            y_delta = abs(points[i + 1][1] - points[i][1])
            t += max(x_delta, y_delta)
        return t


if __name__ == '__main__':
    sl = Solution()
    points = [[3, 2], [-2, 2]]
    null = [[3, 2]]
    tmp = sl.minTimeToVisitAllPoints(null)
    print(tmp)
