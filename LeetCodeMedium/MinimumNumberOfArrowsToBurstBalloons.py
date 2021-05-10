class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x : x[1])
        print(points)
        lastHigh = points[0][1]
        count = 1
        for point in points[1:]:
            if lastHigh >= point[0]:
                pass
            else:
                count += 1
                lastHigh = point[1]
        return count
s = Solution()
res = s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])
print(res)
        