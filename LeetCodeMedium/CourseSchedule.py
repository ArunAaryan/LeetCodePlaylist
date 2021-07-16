from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[src].append(dest)
        visited = [0] * numCourses
        # 1 means visited and no cycle
        # -1 means visited and cycle found or currently visiting from
        # 0 means not visited
        def dfs(root):
            if visited[root] == -1:
                return False
            if visited[root] == 1:
                return True
            # current visiting element is being set to point of cycle until it is proven not.
            # i.e if root is calling itself due to cyles after child explorations
            #  1-> 4 , 4 -> 5 and 5-> 1
            visited[root] = -1
            for node in graph[root]:
                if not dfs(node):
                    return False
            visited[root] = 1
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
s = Solution()
res = s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
print(res) 