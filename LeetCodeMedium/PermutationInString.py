# https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained/
from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        firstPattern = Counter(s1)
        dynamicPattern = Counter(s2[:len(s1)])
        if firstPattern == dynamicPattern:
            return True
        startIdx = 0
        # endIdx will be ending of the current dynamicPattern.
        for endIdx, value in enumerate(s2[len(s1):]):
            # it will start from the length of pattern
            # s2[startIdx : endIdx] will be the sliding window or "dynamicPattern"
            dynamicPattern[value] += 1
            currStartValue = s2[startIdx]
            dynamicPattern[currStartValue] -= 1
            if not dynamicPattern[currStartValue]:
                dynamicPattern.pop(currStartValue)
            startIdx += 1
            if firstPattern == dynamicPattern:
                return True
        return False

    def checkInclusion2(self, s1, s2):
        count, word_len, matched = Counter(s1), len(s1), 0
        for cur in range(len(s2)):
            current_char = s2[cur]
            if current_char in count:
                count[current_char] -= 1
                if count[current_char] == 0:
                    matched += 1
            if cur >= word_len and  s2[cur - word_len] in count:
                if s2[cur - word_len] == 0:
                    matched -= 1
                count[s2[cur - word_len]] += 1
            if matched == len(count):
                return True
        return False

                



s = Solution()
res = s.checkInclusion('arun', 'asdfnura')
print(res)
