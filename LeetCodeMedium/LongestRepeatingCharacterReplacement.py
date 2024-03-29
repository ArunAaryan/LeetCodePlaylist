# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91301/Awesome-python-solution
import collections
def charReplace(string, replaces):
    count = {}
    start = maxcount = 0
    for end in range(len(string)):
        count[string[end]] = count.get(string[end], 0) + 1
        maxcount = max(maxcount, count[string[end]])
        #max count stores the value count which is repeated more than any other character
        #end - start has chars which are repeated and non repeated.
        #ex AAABBACAAB here max count stores count values of A
        if end - start + 1 - maxcount > replaces:
            count[string[start]] -= 1
            start += 1
    return end - start + 1
   
res = charReplace('abas', 1)
print(res)

def characterReplacement(self, s, k):
        count = collections.Counter()
        start = result = 0
        for end in range(len(s)):
            count[s[end]] += 1
            max_count = count.most_common(1)[0][1] # mostcommon returns an array but using (1) limits only results in reduced space complexity.
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result