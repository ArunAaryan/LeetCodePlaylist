from collections import Counter
class Solution:
    # below solution will work for 'atmost k ' unique elements
    # space complexity will depend on k
    def totalFruit(self, tree):
        left = 0
        right = 0
        res = 0
        uniqueCount = Counter()
        while right < len(tree):
            uniqueCount[tree[right]] += 1
            while len(uniqueCount) > 2:
                uniqueCount[left] -= 1
                if not uniqueCount[tree[left]]:
                    uniqueCount.pop(tree[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        print(tree[left : right + 1])
        return res

s = Solution()
res = s.totalFruit([0,1,2,2])
print(res)

        



        