from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Create a dictionary to keep track of the frequency of each word
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1

        # Get the length of each word
        word_len = len(words[0])

        # Get the total length of all the words combined
        total_len = len(words) * word_len

        # Create a list to store the starting index of each substring that contains all the words
        result = []

        # Iterate through each substring of length `total_len` in the input string `s`
        for i in range(len(s) - total_len + 1):
            # Get the current substring
            substring = s[i:i+total_len]

            # Create a dictionary to keep track of the frequency of each word in the current substring
            substring_freq = defaultdict(int)
            for j in range(0, total_len, word_len):
                # Get the current word in the substring
                word = substring[j:j+word_len]
                # Increment the frequency of the current word in the dictionary
                substring_freq[word] += 1

            # If the frequency of each word in the current substring is equal to the frequency of each word in `words`,
            # then add the starting index of the substring to the `result` list
            if substring_freq == word_freq:
                result.append(i)

        # Return the list of starting indices of substrings that contain all the words
        return result
