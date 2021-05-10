from collections import Counter
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks, n):
        wordOccurences= Counter(tasks).values()
        currentIndex = 0
        heap = []
        for frequency in wordOccurences:
            heappush(heap, -1 * frequency)
        while heap:
            remainingTasks = []
            for _ in range(n + 1): # for n = 2 this loop will run for 0, 1, 2 , first time for executing the letter and next two times is the cool down.
                currentIndex += 1
                if heap:
                    ntasks = heappop(heap) 
                    if ntasks != -1:
                        remainingTasks.append(ntasks + 1) # decrease tasks by 1 , + 1 because items are negated for the use of min heapj
                if not heap and not remainingTasks:
                    break
            for remaining in remainingTasks:
                heappush(heap, remaining)      
        return currentIndex




s = Solution()
res = s.leastInterval(["A","A","A","B","B","B"], 2)
print(res)

        