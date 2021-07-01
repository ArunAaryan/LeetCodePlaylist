from typing import List
class Solution:
    def __init__(self):
        self.matrix = None

    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        row_set = set()
        col_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_set or j in col_set:
                    matrix[i][j] =0

    def setZeroesOptimized(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        isCol = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1,C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        self.printMatrix() 
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0 
        
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        if isCol:
            for i in range(R):
                matrix[i][0] = 0
                
# another intuitive approach
def setMatrixZeroes(arr):
    r = len(arr)
    c = len(arr[0])
    isCol = False
    isRow = False
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                if i == 0:
                    isRow = True
                if j == 0:
                    isCol = True
                arr[i][0] = arr[0][j] = 0

    for i in range(1, r):
        for j in range(1, c):
            if arr[i][0] == 0 or arr[0][j]==0:
                arr[i][j] = 0

    if isRow:
        print('isrow')
        for i in range(c):
            arr[0][i] = 0
    
    if isCol:
        for i in range(r):
            arr[i][0] = 0

    for i in range(len(arr)):
            for j in range(len(arr[0])):
                print(arr[i][j], end=" ")
            print("")


    def printMatrix(self):
        matrix = self.matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print("")

s = Solution()
s.setZeroesOptimized([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])
s.printMatrix()
