from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pacific_coords = deque() 
        atlantic_coords = deque()
        for i in range(rows):
            pacific_coords.append((i, 0))
            atlantic_coords.append((i, cols -1))
        
        for i in range(cols):
            pacific_coords.append((0, i))
            atlantic_coords.append((rows-1, i))
        
        def bfs(queue):
            visited = set()
            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for x, y in directions:
                    adj_row = row + x
                    adj_col = col + y
                    if adj_row < 0 or adj_col < 0 or adj_row >= rows or adj_col >= cols:
                        continue
                    if (adj_row, adj_col) in visited:
                        continue
                    if heights[adj_row][adj_col] >= heights[row][col]:
                        queue.append((adj_row, adj_col))
            return visited

        pacific_paths = bfs(pacific_coords)
        atlantic_paths = bfs(atlantic_coords)
        # print(pacific_paths)
        return list(pacific_paths.intersection(atlantic_paths))

    def pacificAtlanticDfs(self, heights):
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for (x, y) in directions:
                adj_row = row + x
                adj_col = col + y
                if adj_row < 0 or adj_col < 0 or adj_row >= rows or adj_col >= cols:
                    continue
                if (adj_row, adj_col) in reachable:
                    continue
                if heights[adj_row][adj_col] >= heights[row][col]:
                    dfs(adj_row,adj_col, reachable)
        
        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols-1, atlantic_reachable)
        
        for i in range(cols):
            dfs(0, i, pacific_reachable)
            dfs(rows -1, i, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))

            
s = Solution()
# res = s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
res = s.pacificAtlanticDfs([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(res)
        