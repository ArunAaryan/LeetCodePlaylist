class Solution:
    def eraseOverlapIntervals(self, intervals):
        res = 0
        intervals.sort(key = lambda x : x[1])# after sorting the first element's end will be the smallest end and its start will obviously be smaller than its end. 
        # so sorting like this will result in intervals sorted in order of their interval difference.
        # so we keep the shortest intervals and eliminate the larger ones and eliminating the larger ones means that we are altering the list by minimum
        #removing smaller overlapping number ranges > removing one large big overlap. 
        # so that is what we want to achieve. to find minimum intervals that are to be removed.
        print(intervals)
        prev = intervals[0][1] # first end
        for interval in intervals[1:]:
            if prev <= interval[0]:
                prev = interval[1]
            else:
                res += 1
        return res

s = Solution()
res = s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])
print(res)


        