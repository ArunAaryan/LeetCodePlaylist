from collections import deque
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1
        return count

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or  grid[i][j] != "1":
            return 
        grid[i][j] = "#"
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        for (x, y) in directions:
            self.dfs(i + x, j + y, grid)

    def numIslandsbfs(self, grid):
        if not grid:
            return 0
        qu = deque([])
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [([False] * (cols)) for _ in range((rows)) ]
        for i in range(rows):
            for j in range(cols):
                if  grid[i][j] == "1" and not visited[i][j]:
                    qu.append((i, j))
                    visited[i][j] = True
                    self.bfs(grid, qu, visited)
                    count += 1
        return count
    
    def bfs(self, grid, qu, visited):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        while qu:
            i, j = qu.popleft()
            for x, y in directions:
                adj_row, adj_col = i + x, j + y
                if adj_row < 0 or adj_col < 0 or adj_row >= rows or adj_col >= cols or visited[adj_row][adj_col] or grid[adj_row][adj_col] == "0":
                    continue
                visited[adj_row][adj_col] = True
                qu.append((adj_row,adj_col))

s = Solution()
# res = s.numIslands([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ])
# res = s.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ])
# print(res)

print(s.numIslandsbfs([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"]
]))

                