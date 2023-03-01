# https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems/?orderBy=most_votes
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ln_s = len(s)
        ln_t = len(t)
        if ln_s == 0 or ln_t == 0 or ln_t > ln_s:
            return ""
        dct = {}
        for ch in t:
            dct[ch] = dct.get(ch, 0) + 1
        
        i = j = 0
        minWindow = ln_s + 1
        output = ""
        
        #ln_t will act as my counter.
        while i < ln_s:
            if s[i] in dct:
                # count how many needed chars are decremented
                if dct[s[i]] > 0:
                    ln_t -= 1
                    
                # decrement from the dict even if it leads to negative
                # so that I can take care of cases such as "AZBBCA" where I
                # need to find "ABC"
                dct[s[i]] -= 1
            
            # shrink the window size
            # and get the result and make it non-valid window
            # so that I can look forward
            while ln_t == 0:
                if i - j + 1 < minWindow:
                    minWindow = i - j + 1
                    output = s[j: i+1]
                
                if s[j] in dct:
                    dct[s[j]] += 1
                    
                    # I added a char from shrinking window
                    # which is needed for me to get "T"
                    if dct[s[j]] > 0:
                        ln_t += 1
                    
                j += 1
                    
            i += 1
        
        return "" if minWindow == ln_s + 1 else output
        