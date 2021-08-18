# https://leetcode.com/problems/sudoku-solver/discuss/15853/Simple-and-Clean-Solution-C%2B%2B
class Solution:
    def solveSudoku(self, board):
        self.board = board
        def validate(row, col, val): 
            for i in range(9):
                if self.board[row][i] == val:
                    return False 
            for i in range(9):
                if self.board[i][col] == val:
                    return False
            row_base = row - row % 3
            col_base = col - col % 3
            for row_offset in range(3):
                for col_offset in range(3):
                    if self.board[row_offset + row_base][col_offset + col_base] == val:
                        return False
            return True
        def solveSudokuHelper(row, col):
            if row == 9:
                return True
            if col == 9 : 
                return solveSudokuHelper(row + 1, 0)
            if self.board[row][col] != ".":
                return solveSudokuHelper(row, col + 1)
            
            for val in "123456789":
                if validate(row, col, val):
                    self.board[row][col] = val
                    if solveSudokuHelper(row, col + 1):
                       return True
                    self.board[row][col] = "."
            return False
        print(solveSudokuHelper(0,0))
        for row in self.board:
            print(row)
        return self.board
s = Solution()
res = s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

assertion = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
print(res == assertion)



