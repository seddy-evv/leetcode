# Task description:
# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


# Sliding Window (with Maximum Frequency Tracking) technique.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency map to count characters in the current window
        char_counts = {}

        left = 0
        max_freq = 0
        max_length = 0

        # Expand the window using the right pointer
        for right, char in enumerate(s):
            # Update the character's frequency count
            char_counts[char] = char_counts.get(char, 0) + 1

            # Track the maximum frequency of any single character seen in the current window
            max_freq = max(max_freq, char_counts[char])

            # Current window size is (right - left + 1)
            # The number of characters we need to replace is (window size - max_freq)
            # If insertions needed exceed k, we must shrink the window from the left
            if (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1

            # Update the maximum valid window size found so far
            max_length = max(max_length, right - left + 1)

        return max_length


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))  # Output: 4
    print(sol.characterReplacement("AABABBA", 1))  # Output: 4


# Time Complexity: O(N), where N is the length of the string s. The right pointer iterates through the string exactly
# once. The left pointer only ever increments forward, meaning each character is processed at most twice.
# Space Complexity: O(1) auxiliary space. Since the input string consists only of uppercase English letters,
# the char_counts dictionary will contain at most 26 unique keys, consuming constant space regardless of how large
# the string grows.
