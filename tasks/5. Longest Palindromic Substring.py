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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        max = ""
        for n in range(len(s)):
            for j in range(len(s) - 1, n - 1, -1):
                last = None if n - 1 < 0 else n - 1
                if s[n:j + 1] == s[j:last:-1]:
                    if len(max) < len(s[n:j + 1]):
                        max = s[n:j + 1]
        return max
