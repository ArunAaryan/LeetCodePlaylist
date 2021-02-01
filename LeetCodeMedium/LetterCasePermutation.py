from typing import List
class Solution:
    
    def letterCasePermutation(self, S: str) -> List[str]:
        res =[]
        self.backtrack(list(S), 0, res)
        return res
         
    
    def backtrack(self, S, idx, res):
        if idx >= len(S):
            res.append("".join(S))
            return
        
        if S[idx].isnumeric():
            self.backtrack(S, idx + 1, res)
        
        else:
            S[idx] = S[idx].upper()
            self.backtrack(S, idx + 1, res)
            S[idx] = S[idx].lower()
            self.backtrack(S, idx + 1, res)
            
            
            