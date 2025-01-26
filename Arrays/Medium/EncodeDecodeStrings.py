# https://neetcode.io/problems/string-encode-and-decode
class Solution:

    def encode(self, strs) -> str:
        if not str:
            return ""
        res = ""
        for s in strs:
            res += str(len(s))
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s):
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != "#":
            size_string = ""
            while (
                s[i] != ","
            ):  # the reason we loop ',' and '#' loop is for 1 word encoded and decoded
                size_string += s[i]
                i += 1
            sizes.append(int(size_string))
            i += 1
        i += 1  # because we are on the delimeter now
        for size in sizes:
            res.append(s[i : i + size])
            i += size
        return res


s = Solution()
encoded = s.encode(strs=["neet", "code", "love", "you"])
print(encoded)
