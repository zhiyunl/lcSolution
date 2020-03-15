"""
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Corner:
    1. row, just return 
    2. col, transpose and return
    Note: 0 > None, but bool(0) is False
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # brute force
        # traversal along the encounter and visit node
        # mark visited nodes as None,
        # flag direction, start from right, then dn, then left, then up, change direction when None or boundary encountered
        if len(matrix) ==0:
            return matrix
        elif len(matrix)==1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]
        m = len(matrix)
        n = len(matrix[0])

        res = [matrix[0][0]]
        dire = 0
        cur = [0, 0]
        matrix[0][0]=None
        while True:
            while dire == 0:
                cur[1] += 1
                if cur[1] < n and matrix[cur[0]][cur[1]]!= None:
                    res.append(matrix[cur[0]][cur[1]])
                    matrix[cur[0]][cur[1]]=None
                else:
                    cur[1] -= 1
                    dire = (dire+1) % 4
            while dire == 1:
                cur[0] += 1
                if cur[0] < m and matrix[cur[0]][cur[1]] != None:
                    res.append(matrix[cur[0]][cur[1]])
                    matrix[cur[0]][cur[1]]=None
                else:
                    cur[0] -= 1
                    dire = (dire+1) % 4
            while dire == 2:
                cur[1] -= 1
                if cur[1] >= 0 and matrix[cur[0]][cur[1]]!= None :
                    res.append(matrix[cur[0]][cur[1]])
                    matrix[cur[0]][cur[1]]=None
                else:
                    cur[1] += 1
                    dire = (dire+1) % 4
            while dire == 3:
                cur[0] -= 1
                if cur[0] >= 0 and matrix[cur[0]][cur[1]]!= None :
                    res.append(matrix[cur[0]][cur[1]])
                    matrix[cur[0]][cur[1]]=None
                else:
                    cur[0] += 1
                    dire = (dire+1) % 4
            # finished a circle, check next pos
            if cur[1]+1 >= n or matrix[cur[0]][cur[1]+1] == None:
                break
        return res
        # Do it layer by layer could be faster


if __name__ == '__main__':
    sl = Solution()
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    num1 = [[1,2,3,4]]
    num2 = [[2,5],[8,4],[0,-1]]
    num3 = [[1],[2],[3]]
    num4=[]
    tmp = sl.spiralOrder(nums)
    print(sl.spiralOrder(num1))
    print(sl.spiralOrder(num2))
    print(sl.spiralOrder(num3))
    print(sl.spiralOrder(num4))
    assert tmp == [1,2,3,6,9,8,7,4,5]
    print(tmp)
