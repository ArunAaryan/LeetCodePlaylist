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
        # check for current interval upper bound overlap
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                # current interval is smaller insert interval and no overlap
                res.append(interval)
            # there is other possibilit of lower bound being overlapped

        # check for current interval lower bound overlap
            # current Interval is (5,6) but newInterval is (1,4) then we can simply append all the remaining intervals.
            elif newInterval[1] < interval[0]:
                # current interval is larger than insert interval
                res.append(newInterval)
                # 1. since we already checked for upper bound only possibility is lower bound
                # 2. if insert interval's first value is still less than current interval's start value means no overlap is possible
                # so we append insert interval first and append all other intervals
                return res + intervals[index:]
            # if the above condition failed, the only possibility is the current interval is in overlap with the insert interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res


s = Solution()
res = s.insert([[1, 3], [6, 9]], newInterval=[2, 5])
print(res)
