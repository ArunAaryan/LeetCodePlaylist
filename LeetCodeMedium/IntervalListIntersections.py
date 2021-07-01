class Solution:
    def intervalIntersection(self, firstList, secondList):
        j = 0
        i = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if lo <= high: # means when there is intersection only then append
                res.append([lo, high])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res

s = Solution()
res = s.intervalIntersection([[5,5],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]])
print(res)


        
        