from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and self.dfs(i, j, 0, board, word):
                    return True
        return False

    def dfs(self, i, j, nwords, board, word):
        if nwords == len(word):
            return True 
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[nwords]:
            return False

        temp = board[i][j] 
        board[i][j] = "#"
        foundWord = self.dfs(i + 1, j, nwords + 1, board, word) or self.dfs(i - 1, j, nwords + 1, board, word) or self.dfs(i, j-1, nwords + 1, board, word) or self.dfs(i, j+1, nwords + 1, board, word)
        
        board[i][j] = temp
        return foundWord

s = Solution()
res = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")
print(res)
        