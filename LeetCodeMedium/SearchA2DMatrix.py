class Solution:
    def searchMatrix(self, matrix, target):
        row  = len(matrix) - 1
        col = 0
        while  row >= 0 and col < len(matrix[0]): 
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
    # if we want to find the 4th element of 4 x 3 matrix. the row = 4 // 3 = 1, col = 4 % 3 = 1.
    # 1 2 3 
    # 5 6 7
    # 8 9 10
    # 11 12 13
    # so the element will be at 1,1 .
    # index / numberOfCols => which row
    # index % numberOfCols => which col
    def searchMatrixBinary(self, matrix, target):
        cols = len(matrix[0])
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols 
            col = mid % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
                


s = Solution()
res = s.searchMatrixBinary([[1,3]], target = 3)
print(res)


