# Task description:
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


# Frequency Counting via Greedy Character Pairing.
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Count the occurrences of each character
        char_counts = Counter(s)

        palindrome_length = 0
        has_odd_frequency = False

        # Step 2: Greedily pair up characters
        for count in char_counts.values():
            # If the count is even, all characters can be matched symmetrically
            # If the count is odd, we take the largest even part (count - 1)
            palindrome_length += (count // 2) * 2

            # Track if there is at least one odd count remaining to place in the center
            if count % 2 == 1:
                has_odd_frequency = True

        # Step 3: If an odd frequency exists, we can place exactly one unique character in the center
        if has_odd_frequency:
            palindrome_length += 1

        return palindrome_length


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 matching Example 1
    input_str1 = "abccccdd"
    result1 = sol.longestPalindrome(input_str1)
    print(f"String: '{input_str1}' -> Longest Palindrome Length: {result1}")
    # Output: 7

    # Test Case 2 matching Example 2
    input_str2 = "a"
    result2 = sol.longestPalindrome(input_str2)
    print(f"String: '{input_str2}' -> Longest Palindrome Length: {result2}")
    # Output: 1


# Time Complexity: O(N), where N is the length of the string s. The algorithm scans the string exactly once to populate
# the frequency map and then iterates over the distinct character keys. Since the size of the alphabet is fixed
# (at most 52 unique uppercase and lowercase English characters), the dictionary loop runs in O(1) auxiliary time.
# Space Complexity: O(1) auxiliary space. Although we initialize a Counter hash map, it stores a maximum of 52 unique
# character counts. Because this storage bound is constant and completely independent of the size of the input string
# length N, the space complexity remains constant.
