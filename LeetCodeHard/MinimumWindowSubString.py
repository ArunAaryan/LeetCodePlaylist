from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Get the length of the input strings
        s_len = len(s)
        t_len = len(t)

        # Check if the input strings are valid
        if s_len == 0 or t_len == 0 or t_len > s_len:
            return ""

        # Create a dictionary to count the occurrences of each character in the target string
        target_dict = Counter(t)

        # Initialize the pointers, minimum window size and output string
        left = right = 0
        min_window = s_len + 1
        output = ""

        # Initialize a counter to keep track of the remaining characters that need to be found
        remaining_chars = t_len

        # Move the right pointer to find all the characters of the target string
        while right < s_len:
            # If the current character is in the target string, decrement its count and update the remaining characters counter
            if s[right] in target_dict:
                if target_dict[s[right]] > 0:
                    remaining_chars -= 1
                target_dict[s[right]] -= 1

            # If all the characters of the target string have been found, move the left pointer to shrink the window
            while remaining_chars == 0:
                # Update the minimum window size and output string
                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    output = s[left: right+1]

                # If the current character is in the target string, increment its count and update the remaining characters counter
                if s[left] in target_dict:
                    target_dict[s[left]] += 1
                    if target_dict[s[left]] > 0:
                        remaining_chars += 1

                # Move the left pointer to shrink the window
                left += 1

            # Move the right pointer to expand the window
            right += 1

        # Return the output string if a valid minimum window substring was found
        return output if min_window != s_len + 1 else ""

s = Solution()
s.minWindow(s = "ADOBECODEBANC", t = "ABC")