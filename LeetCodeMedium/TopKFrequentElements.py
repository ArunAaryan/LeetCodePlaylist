from heapq import nlargest 
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        return nlargest(k, c.keys(), key = c.get)
    # n buckets solution
    # https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = defaultdict(int)
        for num in nums:
            countFreq[num] += 1
        bucketList = [[] for _ in range(len(nums) + 1) ]
        for num, freq in countFreq.items():
            bucketList[freq].append(num)
        
        flatList = []
        for bucket in bucketList:
            if bucket:
                for val in bucket:
                    flatList.append(val)
        return flatList[::-1][:k]
        




s = Solution()
res = s.topKFrequent([3,0,1,0],2)
print(res)


        