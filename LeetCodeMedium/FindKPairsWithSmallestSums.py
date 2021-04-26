import heapq
class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     heap = []
    #     ans =  []

    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             heapq.heappush(heap, (nums1[i] + nums2[j], nums1[i], nums2[j]))

    #     k = min(k, len(heap))
    #     for _ in range(k):
    #         res = heapq.heappop(heap)
            # ans.append([res[1], res[2]])

    def kSmallestOptimized(self, nums1, nums2, k):
        if not nums1 or not nums2 or not k :
            return []
        visited = set() 
        # why visited for such an input below we can reduce the repeating chars
        # [1,1,2]
        #  [1,2,3]
        #     10
        answer = []
        heap = []
        n1l = len(nums1)
        n2l = len(nums2)
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))
        while heap and len(answer) < k:
            s, first, second = heapq.heappop(heap)
            answer.append([nums1[first], nums2[second]])
            if first + 1 < n1l and (first + 1, second) not in visited:
                heapq.heappush(heap, (nums1[first + 1] + nums2[second], first + 1, second))
                visited.add((first + 1, second))
            
            if second + 1 < n2l and (first, second + 2) not in visited:
                heapq.heappush(heap, (nums1[first] + nums2[second + 1], first, second + 1))
                visited.add((first, second + 1))

        return(answer)

s = Solution()
res = s.kSmallestOptimized(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
print(res)