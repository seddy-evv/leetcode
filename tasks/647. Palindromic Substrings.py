# Task description:
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


# Expand Around Center.
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0

        def expand_and_count(left: int, right: int) -> int:
            """
            Expands outward from a center and counts all valid palindromes.
            """
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            # Case 1: Odd-length palindromes (single character center, e.g., "aba")
            total_palindromes += expand_and_count(i, i)

            # Case 2: Even-length palindromes (between two characters center, e.g., "abba")
            total_palindromes += expand_and_count(i, i + 1)

        return total_palindromes


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))
    # Output: 3
    print(sol.countSubstrings("aaa"))
    # Output: 6


# Time Complexity: O(N^2), where N is the length of the string s. There are 2N - 1 possible center points to expand
# from. For each center, expanding outward takes up to O(N) comparisons in the worst case, making it much more
# efficient than the naive O(N^3) approach.
# Space Complexity: O(1) auxiliary space. The check runs completely in-place using index pointer updates without
# allocating dynamic arrays or extra sub-string storage blocks.
