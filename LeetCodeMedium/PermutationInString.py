from collections import Counter
class Solution:
	def checkInclusion(self, s1, s2):
        firstPattern = Counter(s1)
        dynamicPattern =  Counter(s2[:len(s1)])
        if firstPattern == dynamicPattern:
            return True
        startIdx = 0
        for endIdx, value in enumerate(s2[len(s1):]): #endIdx will be ending of the current dynamicPattern.
        #it will start from the length of pattern
        # s2[startIdx : endIdx] will be the sliding window or "dynamicPattern"
            dynamicPattern[value] +=  1
            currStartValue = s2[startIdx] 
            dynamicPattern[currStartValue] -= 1
            if not dynamicPattern[currStartValue]:
                dynamicPattern.pop(currStartValue)
            startIdx += 1
            if firstPattern == dynamicPattern:
                return True
        return False
s = Solution()
res = s.checkInclusion('arun','asdfnura')
print(res)
		












