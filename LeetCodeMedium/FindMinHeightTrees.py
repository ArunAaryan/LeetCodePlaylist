class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return[vertex for vertex in range(n)]
            # if there are only two vertices then both vertices can form minimal height tree if selected
        adj = [set() for _ in range(n)] 
        for src, dest in edges:
            adj[src].add(dest)
            adj[dest].add(src)
        # adjacent list for all the vertices
        leaf_nodes = []
        for node in range(n):
            if len(adj[node]) == 1:
                leaf_nodes.append(node)
        
        remaining_nodes = n 
        while remaining_nodes > 2: 
            remaining_nodes -= len(leaf_nodes)
            new_leaf_nodes = []
            while leaf_nodes:
                cur_leaf = leaf_nodes.pop()
                neighbour_node = adj[cur_leaf].pop()
                adj[neighbour_node].remove(cur_leaf)
                if len(adj[neighbour_node]) == 1:
                    new_leaf_nodes.append(neighbour_node)
            leaf_nodes = new_leaf_nodes
        return leaf_nodes
    

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    seen = [False] * n
    
    def dfs(i):
        if seen[i] : return []
        longestPath = []
        seen[i] = True
        for adj in graph[i]:
            if not seen[adj]:
                path = dfs(adj)
                if len(path) > len(longestPath):
                    longestPath = path
        longestPath += [i]
        seen[i] = False
        return longestPath
    
    path = dfs(0)
    
    longestPath = dfs(path[0])
    return set([longestPath[len(longestPath) // 2 ], longestPath[(len(longestPath) - 1 ) // 2]])
    
s = Solution()
res = s.findMinHeightTrees(6,[[0,1],[0,2],[1,3],[1,4],[3,5]])
print(res)


        
        

        