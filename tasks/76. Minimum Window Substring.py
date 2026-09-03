# Task description:
# GGiven two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?


# Sliding Window with Two Pointers and Frequency Map Tracking.
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Dictionary to store the frequency of characters required from t
        target_counts = Counter(t)
        # Unique characters in t that must match in the window
        required_unique_chars = len(target_counts)

        # Dictionary to keep track of character frequencies in the current window of s
        window_counts = {}
        # Tracks how many unique characters meet their target frequency requirements
        formed_unique_chars = 0

        # Tuple to store window details: (window_length, left_index, right_index)
        ans = (float("inf"), None, None)

        left = 0
        # Expand the window using the right pointer
        for right, char in enumerate(s):
            # Update the count of the current character in the window
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character match count satisfies the requirement in t
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed_unique_chars += 1

            # Try to shrink the window from the left once all requirements are met
            while left <= right and formed_unique_chars == required_unique_chars:
                left_char = s[left]

                # Update the smallest window seen so far
                current_window_len = right - left + 1
                if current_window_len < ans[0]:
                    ans = (current_window_len, left, right)

                # Evict the leftmost character and move the left pointer forward
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed_unique_chars -= 1

                left += 1

        # Return the minimum substring, or empty string if no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    # Output: "BANC"


# Time Complexity: O(M + N), where M is the length of string s and N is the length of string t. Creating the frequency
# map for t takes O(N) time. Each character in s is processed at most twice (once by the right pointer and once by
# the left pointer), taking O(M) time total.
# Space Complexity: O(M + N) worst-case auxiliary space. The target_counts map stores up to N distinct entries,
# while the window_counts map holds up to M distinct characters in the worst-case scenario.
