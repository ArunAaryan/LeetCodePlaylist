# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/949552/python-sliding-window-solution-explained/?orderBy=most_votes
from collections import Counter
class Solution:
    def longestSubstring(self, s, k):
        result = 0 # will store the max substring len
        for T in range(1, len(Counter(s)) + 1): # run for len of number of unique characters 
            # T is the number of unique characters we want to consider for current window
            beg, end, found, freq_arr, more_equal_k = 0, 0, 0, [0] * 26, 0
            while end < len(s):
                if more_equal_k <= T: # while number of chars satisfying atleast 'k' condition is less than T
                    new_char = ord(s[end]) - 97
                    freq_arr[new_char] += 1
                    if freq_arr[new_char] == 1: # if the current char entered first time
                        more_equal_k += 1
                    if freq_arr[new_char] == k:
                        found += 1
                    end += 1
                else: # we have more different elements than we are considering in the current window
                    char = ord(s[beg]) - 97
                    beg += 1 # move the window to the right
                    if freq_arr[char] == k:
                        found -= 1
                    freq_arr[char] -= 1
                    if freq_arr[char] == 0: # if the char is not longer in the window, remove from non zero count
                        more_equal_k -= 1
                if more_equal_k == T and found == T: # if the window consists of T different unique characters and all those characters meet min k requirement
                    result = max(result, end - beg)
            return result







