# Suppose there is an array of meeting time intervals. 
# There are two times start and end times [[s1,e1],[s2,e2],...] and each pair satisfies the rule (si < ei), 
# We have to find the minimum number of conference rooms required.
import heapq
class Solution:
    def MeetingRooms2(self, intervals):
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        heap = [intervals[0][1]]
        for interval in intervals[1:]:
            lastEnding = heapq.heappop(heap)
            if interval[0] >= lastEnding:
                lastEnding = interval[1]
            else:
                heapq.heappush(heap, interval[1])
            heapq.heappush(heap, lastEnding)
        return len(heap)




s = Solution()
# res = s.MeetingRooms2([[0, 30],[5, 10],[15,20]])
res = s.MeetingRooms2([[2,17],[2,19],[36,45],[9,29],[16,23],[4,9]])
# res = s.MeetingRooms2([[2,17],[2,19]])
print(res)
