class Solution:
    def meetingRooms(self, intervals):
        intervals.sort(key = lambda x : x[0])
        prev = intervals[0][1]
        for interval in intervals[1:]:
            if prev > interval[0]:
                return False
        
        return True

s = Solution()
# res = s.meetingRooms([ [0, 30], [5, 10], [15, 20] ])
res = s.meetingRooms([[10,20], [0,10],[21,30]])

print(res)