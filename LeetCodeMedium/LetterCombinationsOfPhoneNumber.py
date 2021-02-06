from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination, index):
            if index == len(digits):
                res.append(combination[:])
                return 
            else:
                for letter in phone[digits[index]]:
                    backtrack(combination + letter, index + 1)




        res = []
        phone = {'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        backtrack("",0)
        return res

s = Solution()
res =  s.letterCombinations('23')
print(res)



        