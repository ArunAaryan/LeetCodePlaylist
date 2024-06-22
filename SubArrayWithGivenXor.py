class Solution:

    def findSubArrayWithXor(self, arr, target):
        xor_map = {}  # to store each new xor value's count
        prefix_xor = 0  # to store xor of all values till the element
        count = 0  #
        for num in arr:
            prefix_xor ^= num

            if (
                prefix_xor == target
            ):  # if prefix_xor from index '0' to current element matches then
                count += 1

            if (
                prefix_xor ^ target
            ) in xor_map:  # means that the current num ^ (some previous num) = target exists in the map
                count += xor_map[prefix_xor ^ target]

            # if seen this 'prefix_xor' previously then increase its occurence count in map;
            # also means to get this 'prefix_xor' there is a now new subarray
            if prefix_xor in xor_map:
                xor_map[prefix_xor] += 1
            else:
                xor_map[prefix_xor] = 1

        return count


s = Solution()
res = s.findSubArrayWithXor([4, 2, 2, 6, 4], 6)
print(res)
