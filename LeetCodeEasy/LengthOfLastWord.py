class Solution:
    def lengthOfLastWord(self, s):
        max_count = 0
        count = 0
        for val in s:
            if val == " ":
                count = 0
            else:
                count += 1
            max_count = count or max_count
        return max_count

s = Solution()
ans = s.lengthOfLastWord("luffy is still joyboy1")
print(ans)


