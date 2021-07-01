from typing import List
# Random user's code python
class Solution:
    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print("")
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res
    
    def spiralOrder1(self, matrix):
        res = []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while left <=right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if left > right or top > bottom:
                break
            
            for i in range(right, left-1,-1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top -1, -1):
                res.append(matrix[i][left])
            left += 1
        self.printMatrix(matrix)
        return res

s = Solution()
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
arr = [[1,2,3,4,5]]
arr = [[1],[2],[3]]
res = s.spiralOrder1(arr)
print(res)

        

            




