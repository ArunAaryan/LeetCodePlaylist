from collections import defaultdict
class Solution:
    def isGraphValidTree(self, n, edges):
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest) 
            graph[dest].append(src) 
        visited = set()
        def dfs(root, parent):
            visited.add(root)
            for node in graph[root]:
                if node == parent:
                    continue
                if node in visited:
                    return False
                if not dfs(node, root):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

    # Cycle condition : If ther number of nodes -1 == edges  then there are no cycles
    def isGraphValidTree2(self, n, edges):
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        visited = set()
        def dfs(root):
            visited.add(root)
            for node in graph[root]:
                if node in visited:
                    continue
                dfs(node)
        dfs(0)
        # print(visited)
        return len(visited) == n and len(edges) == n - 1



s = Solution()
res = s.isGraphValidTree2(5, [[0,1],[1,3],[1,2],[1,4]])
print(res)