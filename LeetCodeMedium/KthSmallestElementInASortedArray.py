from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix, k):
        if len(matrix) == 0 or len(matrix[0]) == 0 or k == 0:
            return 
        heap = [(matrix[0][0], 0,0)]
        visited = set()
        visited.add((0, 0))
        while k > 1:
            # print(heappop(heap))
            (element,  row, col) = heappop(heap)
            # print(element, row, col)
            if col + 1 < len(matrix[0]) and (row, col + 1) not in visited:
                heappush(heap, (matrix[row][col+1], row, col + 1))
                visited.add((row, col + 1))
            if row + 1 < len(matrix) and (row + 1, col) not in visited:
                heappush(heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            k -= 1
        return heap[0][0]

    def kthSmallestNaive(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for row in matrix:
            for num in row:
                heappush(heap, num)
        for _ in range(k - 1):
            heappop(heap)
        return heap[0]
        
    def kthSmallestBinarySearch(self, matrix, k):
        if not matrix or not matrix[0] or not k :
            return matrix
        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        def countLessEqual(matrix, mid, smaller,  larger):
                n  = len(matrix)
                row = n - 1
                col = 0
                count = 0
                while row >= 0 and col < n:
                    if matrix[row][col] > mid:
                        larger = min(larger, matrix[row][col])
                        row -= 1
                    else:
                        smaller = max(smaller, matrix[row][col])
                        count += row + 1 # even the rows are in sorted order,
                        #  if the element at current row is smaller than mid then all the above elements in the above rows and same col are also smaller
                        # but row starts from 0 so we add row + 1 which means row + 1 elements above are smaller than mid.
                        col += 1
                return count, smaller, larger

        while start < end:
            mid = start + (end - start) / 2 
            smaller, larger = matrix[0][0], matrix[n-1][n-1]

            
            count, smaller, larger = countLessEqual(matrix, mid, smaller, larger)
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else: 
                end = smaller
        return start


        

s = Solution()
for i in range(9):
    res = s.kthSmallestBinarySearch([[1,5,9],[10,11,13],[12,13,15]], i)
    res = s.kthSmallestBinarySearch([[2,6,8],[3,7,10],[5,8,11]], i)
    print(res)        