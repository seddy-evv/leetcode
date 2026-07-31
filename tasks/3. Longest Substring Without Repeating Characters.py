"""
Given a string s, find the length of the longest  substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


# Sliding Window algo:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the character and its last seen index
        left = 0
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]

            # If character is duplicated inside current window, jump left pointer
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1

            # Update last seen position of the character
            char_map[current_char] = right

            # Calculate current window size and update max
            window_size = right - left + 1
            max_length = max(max_length, window_size)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
    # 3

    
# Complexity Analysis
# Time Complexity: O(N) because the right pointer iterates through the string exactly once. 
# The left pointer only jumps forward and never backtracks.
# Space Complexity: O(min(M,N) where m is the size of the alphabet/character set. 
# The hash map stores at most all unique characters in the string.
