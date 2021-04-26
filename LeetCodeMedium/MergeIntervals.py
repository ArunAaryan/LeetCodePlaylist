class Solution:
    def merge(self, intervals):
        merge = []
        intervals.sort(key = lambda x : x[0])
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge

s = Solution()
res = s.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)


        

        