from typing import List
class Solution:
    def rotateImageWithDuplicateMatrix(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c =len(matrix[0])
        res =[[0] * c for _ in range(r)]

        for j in range(c):
            for i in range(r-1, -1, -1):
                # print(j, r-i-1)
                res[j][r-i-1]= matrix[i][j]
        return res
   #youtube solution
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r:
            top, bottom = l, r
            for i in range(r-l):
                topLeft = matrix[top ][l + i]
                matrix[top][l + 1] = matrix[bottom-1][l]
                matrix[bottom-i][l] = matrix[bottom][r - i]
                matrix[bottom][r -i] = matrix[top + i][r]
                matrix[top + 1][r] = topLeft
            r -= 1
            l += 1
        
    #leetcode user solution
    def rotateLeft(self, matrix):
        #rotate 90 = transpose + reverse
        #transpose the matrix
        row = col = len(matrix)
        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        printmatrix(matrix)
        #reverse the matrix
        for i in range(row):
            for j in range(int(col/2)):
                matrix[i][j], matrix[i][~j] = matrix[i][~j] , matrix[i][j]
        printmatrix(matrix)


                    

def printmatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print("")

s = Solution()
res = s.rotateLeft([[1,2,3],[4,5,6],[7,8,9]])
# printmatrix(res)

        