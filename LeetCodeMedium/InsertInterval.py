from bisect import insort
class Solution:
    def insertIsort(self, intervals, newInterval):
        insort(intervals, newInterval)
        prev = intervals[0][1]
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= prev:
                res[-1][1] = max(interval[1], prev)
            else:
                res.append(interval)
        return res
    def insert(self, intervals, newInterval):
        res = []
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[1] < interval[0]: # current Interval is (5,6) but newInterval is (1,4) then we can simply append all the remaining intervals.
                res.append(newInterval)
                return res + intervals[index:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res
                
s = Solution()
res = s.insert([[1,3],[6,9]], newInterval = [2,5])
print(res)

        