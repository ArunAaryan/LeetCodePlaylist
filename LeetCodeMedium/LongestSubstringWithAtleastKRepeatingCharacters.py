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


    from collections import Counter
    def longestSubstring(self, s: str, k: int) -> int:
        max_substring_len = 0  # will store the max substring len
        for unique_char_count in range(1, len(Counter(s)) + 1):  # run for len of number of unique characters
            # unique_char_count is the number of unique characters we want to consider for current window
            left, right, chars_with_count_at_least_k, char_counts, unique_chars_in_window = 0, 0, 0, Counter(), 0
            while right < len(s):
                if unique_chars_in_window <= unique_char_count:  # while number of unique chars in the current window is less than or equal to unique_char_count
                    char_counts[s[right]] += 1
                    if char_counts[s[right]] == 1:  # if the current char entered first time
                        unique_chars_in_window += 1
                    if char_counts[s[right]] == k:
                        chars_with_count_at_least_k += 1
                    right += 1
                else:  # we have more different elements than we are considering in the current window
                    char_counts[s[left]] -= 1
                    if char_counts[s[left]] == k - 1:
                        chars_with_count_at_least_k -= 1
                    if char_counts[s[left]] == 0:  # if the char is not longer in the window, remove from unique_chars_in_window count
                        unique_chars_in_window -= 1
                    left += 1  # move the window to the right
                if unique_chars_in_window == unique_char_count and chars_with_count_at_least_k == unique_char_count:
                    # if the window consists of unique_char_count different unique characters and all those characters meet min k requirement
                    max_substring_len = max(max_substring_len, right - left)
        return max_substring_len

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        counts = Counter(s)
        least_frequent = min(counts, key=counts.get)
        
        if counts[least_frequent] >= k:
            return len(s)
        
        left = self.longestSubstring(s[:s.index(least_frequent)], k)
        right = self.longestSubstring(s[s.index(least_frequent)+1:], k)
        
        return max(left, right)




