# https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
# https://leetcode.com/problems/find-k-closest-elements/discuss/202785/Very-simple-Java-O(n)-solution-using-two-pointers
class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k #because when we return the arr[mid : mid + k] the final value at pos k is excluded  the final value at pos k is excluded 
        while left < right:
            mid = (left + right ) // 2
            if x - arr[mid] > arr[mid + k] - x: # we use greater because in cases like [1,2,2,2,3,3,3,3]. the mid and mid+k values will be same. 
                #So the only way to move forward is towards right as it is in increasing order. 
                #so if the current mid and mid + 1 are greater then we set left to mid + 1
                left = mid + 1
            else:
                # if the mid and mid + k element are equal then we should include the right element also. 
                right = mid
        return arr[left: left + k]

s = Solution()
res = s.findClosestElements([1,2,3,4,5,6,7,8],3,3)
print(res)
        
