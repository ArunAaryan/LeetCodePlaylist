import heapq
class Solution:
    def MeetingRooms2(self, intervals):
        intervals.sort(key = lambda x : x[0])
        heap = [intervals[0][1]]
        for interval in intervals:
            lastEnding = heapq.heappop(heap)
            if interval[1] >= lastEnding:
                lastEnding = interval[1]
            else:
                heapq.heappush(heap, interval[1])
            heapq.heappush(heap, lastEnding)
        return len(heap)




s = Solution()
res = s.MeetingRooms2([[0, 30],[5, 10],[15,20]])
# res = s.MeetingRooms2([[2,15],[36,45],[9,29],[16,23],[4,9]])
print(res)
