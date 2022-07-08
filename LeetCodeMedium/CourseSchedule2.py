# https://leetcode.com/problems/course-schedule-ii/discuss/266867/Python-Topological-Sort-BFS-and-DFS-(reserve-order)
# https://leetcode.com/problems/course-schedule-ii/discuss/762346/Python-BFS-beats-98-with-Detailed-Explanation-and-Comments!
from collections import defaultdict

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    for src, dest in prerequisites:
        graph[src].append(dest)
    order = []
    visited, visiting, notvisited = 1, -1, 0
    visited_map = [0] * numCourses
    
    def findCycle(src):
        visited_map[src] = visiting
        for dest in graph[src]:
            if visited_map[dest] == visiting or (not visited_map[dest] and findCycle(dest)):
                return True
        visited_map[src] = visited
        order.append(src)
        return False
    
    for src in range(numCourses):
        if not visited_map[src] and findCycle(src):
            return []
    return order

res = findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(res)
