from collections import defaultdict
class Solution:
    def numberOfConnectedComponents(self, n, edges):
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

        count = 0
        for vertex in graph:
            if vertex not in visited:
                dfs(vertex)
                count += 1
        return count

s = Solution()
res = s.numberOfConnectedComponents(5,[[0,1],[2,3],[3,4],[4,5],[7,9]])
print(res)

