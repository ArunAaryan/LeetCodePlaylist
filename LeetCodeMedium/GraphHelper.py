# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def addNode(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)


class Graph:
    def __init__(self):
        self.vertices = {}

    def createNode(self, val):
        if val not in self.vertices: 
            self.vertices[val] = Node(val)
    
    def addEdge(self, src, dest):
        if src in self.vertices and dest in self.vertices:
            self.vertices[src].neighbors.append(self.vertices[dest])
        elif src not in self.vertices:
            self.createNode(src)
            self.vertices[src].neighbors.append(self.vertices[dest])
        elif dest not in self.vertices:
            self.createNode(dest)
            self.vertices[src].neighbors.append(self.vertices[dest])
        
    def getFirstNode(self):
        return self.vertices[1]

    def arrayToGraph(self, arr):
        for val, neighbors in enumerate(arr):
            self.createNode(val+1)
            for neigh in neighbors:
                self.addEdge(val+1, neigh )

    @classmethod
    def bfsGraph(cls, node):
        visited = set({}) 
        visited.add(node)
        q = deque([node])
        print()
        while q:
            cur = q.popleft()
            print(cur.val, end=" ")
            for neigh in cur.neighbors:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
    
    @classmethod
    def dfsGraph(cls, node):
        visited = set({})
        visited.add(node)
        stack = [node] 
        print()
        while stack:
            cur = stack.pop()
            print(cur.val,end=" ")
            
            for neigh in cur.neighbors:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)


graph = Graph()
graph.arrayToGraph([[4,3,2],[4,5],[]])
res = graph.getFirstNode()
Graph().bfsGraph(res)
Graph().dfsGraph(res)
