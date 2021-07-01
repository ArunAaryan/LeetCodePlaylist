from GraphHelper import Graph
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# neighbours = [] or neighbours = [neighbor_node, neighbor_node]

#dfs iterative solution
from collections import deque
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        #mapper which maps the original nodes to the newly created ones
        #mapper also serves as lookup  for visited nodes
        mapper = {node : Node(node.val)}
        #queue to keep track of the elements which are to be visited
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in mapper:
                    mapper[nei] = Node(nei.val)
                    q.append(nei)
                mapper[cur].neighbors.append(mapper[nei])
        return mapper[node]

    def cloneGraphDfs(self,node):
        if not node:
            return None
        stack = [node]
        mapper = {node: Node(node.val)}
        while stack:
            cur = stack.pop()
            for neigh in cur.neighbors:
                if neigh not in mapper:
                    mapper[neigh] = Node(neigh.val) 
                    stack.append(neigh)
                mapper[cur].neighbors.append(mapper[neigh])
        return mapper[node]

        
# graph = Graph()
# graph.arrayToGraph([[2,4],[1,3],[2,4],[1,3]])
# res = graph.getFirstNode()
# Graph().bfsGraph(res)
# s = Solution() 
# res = s.cloneGraph(res)
# Graph().bfsGraph(res)