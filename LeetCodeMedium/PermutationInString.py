# https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained/
from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        firstPattern = Counter(s1)
        dynamicPattern = Counter(s2[: len(s1)])
        if firstPattern == dynamicPattern:
            return True
        startIdx = 0
        # endIdx will be ending of the current dynamicPattern.
        for endIdx, value in enumerate(s2[len(s1) :]):
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
            if cur >= word_len and s2[cur - word_len] in count:
                if s2[cur - word_len] == 0:
                    matched -= 1
                count[s2[cur - word_len]] += 1
            if matched == len(count):
                return True
        return False

    # https://neetcode.io/problems/permutation-string
    def getIndex(self, char):
        return ord("a") - ord(char)

    def checkInclusion3(self, s1, s2):
        if len(s1) > len(s2):  # no chance if s1 is greater than s2
            return False
        s1_count, s2_count = [0] * 26, [
            0
        ] * 26  # initialize lookup table from a..z for both strings
        for idx, val in enumerate(s1_count):
            index1 = self.getIndex(val)
            index2 = self.getIndex(s2[idx])
            s1_count[index1] += 1
            s1_count[index2] += 1
        matches = 0
        for i in range(len(s1_count)):  # or simply range(26)
            if s1_count[i] == s2_count[i]:
                matches += 1
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = self.getIndex(s2[right])
            s2_count[index] += 1  # increase occurrence count of current val
            # check if including current value has caused any matches
            if s2_count[index] == s1_count[index]:
                matches += 1
            # check if including current value has decreased any matches
            elif s2_count[index] - s1_count[index] == 1:
                matches -= 1
            # else part would be simply adding another duplicate occurrence of value in current window, so we skip it

            index = self.getIndex(s2[left])
            # remove the leftmost val from current index
            s2_count[index] -= 1

            #  check if removing the occurrence of the value has caused any matches
            if s1_count[index] == s2_count[index]:
                matches += 1
            #  check if removing the occurrence of the value has decreased any matches
            elif s1_count[index] - s2_count[index] == 1:
                matches -= 1
            l += 1
        return matches == 26


s = Solution()
res = s.checkInclusion("arun", "asdfnura")
print(res)
