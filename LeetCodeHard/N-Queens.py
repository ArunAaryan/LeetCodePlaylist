# https://leetcode.com/problems/n-queens/discuss/19808/Accepted-4ms-c%2B%2B-solution-use-backtracking-and-bitmask-easy-understand.
class Solution:
    def solveNQueens(self, n):
        places = [["."] * n for _ in range(n)]
        # print(places)
        self.res = []
        def isValid(row, col, places, n):
            for r in range(row):
                if places[r][col] == "Q":
                    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if places[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i ,j = row - 1, col + 1
            while i >= 0 and j < n:
                if places[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True


        def solveNQueensHelper(row, places, n):
            if row == n:
                places = ["".join(a) for a in places]
                self.res.append(places)
                return  
            for col in range(n):
                if isValid(row, col, places, n):
                    places[row][col] = "Q"
                    solveNQueensHelper(row + 1,places,n)
                    places[row][col] = "."
        solveNQueensHelper(0, places,n )
        return self.res
    

s = Solution()
res = s.solveNQueens(4)
print(res)