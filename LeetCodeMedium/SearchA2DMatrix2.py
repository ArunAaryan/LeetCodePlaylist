#Binary search  cannot be applied here, but search from bottom of the rows. check if the row starting element is 
# smaller than target, it means that the target element could be in the same row then increase the col 
class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return -1