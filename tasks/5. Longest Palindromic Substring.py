"""
Given a string s, return the longest
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


#  Approach 1: Expand Around Center algo
# (Note: While Manacher's Algorithm runs in pure linear O(N) time, it is highly complex and rarely expected in a live interview setup. 
# The Expand Around Center approach strikes the perfect balance between high performance and flawless readability).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindrome (e.g., "aba", center is s[i])
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindrome (e.g., "abba", center is between s[i] and s[i+1])
            len2 = expand_around_center(i, i + 1)

            max_len = max(len1, len2)

            # Update the boundaries of the longest palindrome found so far
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))
# aba

# Time Complexity: O(N^2), where N is the length of the string s. There are 2N - 1 possible centers to expand from, and each expansion step can 
# take up to O(N) comparisons in the worst case. This easily defeats a naive brute force approach O(N^3).
# Space Complexity: O(1) auxiliary space. The algorithm tracks index pointers (start, end, left, right) natively in memory without introducing
# dynamic arrays or strings during execution.


# Approach 2: Manacher's Algorithm (Linear Time Solution)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Transform string to handle even lengths uniformly (e.g., "aba" -> "^#a#b#a#$")
        # '^' and '$' act as unique bounds to prevent out-of-bounds loop checking
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n  # Array to store palindrome radius at each index
        center = 0
        right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror of i with respect to center

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Attempt to expand the palindrome centered at i
            while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
                p[i] += 1

            # If the expanded palindrome goes beyond right, adjust center and right
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find the maximum radius and its center index
        max_len, center_index = max((val, idx) for idx, val in enumerate(p))

        # Map back to the original string indices
        start = (center_index - max_len) // 2
        return s[start:start + max_len]


sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))
# aba

# Time Complexity: O(n)
# Space Complexity: O(n)
