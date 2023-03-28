# similar to PermutationInString
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        cntr, p_len, match = Counter(p), len(p), 0     
        res = []
        for i in range(len(s)):
            # if the current char is found in counter
            if s[i] in cntr:
                if cntr[s[i]] == 0: 
                    match -= 1
                cntr[s[i]] -= 1
                if cntr[s[i]] == 0: 
                    match += 1

            if i >= p_len and s[i-p_len] in cntr:
                if cntr[s[i-p_len]] == 0: 
                    match -= 1
                cntr[s[i-p_len]] += 1
                if cntr[s[i-p_len]] == 0:
                    match += 1

            if match == len(cntr):
                res.append(i - p_len + 1)
        return res

