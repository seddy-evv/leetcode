# Task description:
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
# in any order.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Constraints:
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


# Sliding Window with Fixed Size and Frequency Counters.
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)

        # If the search string is shorter than the target anagram length, no matches exist
        if s_len < p_len:
            return []

        result = []

        # Initialize frequency counters for lowercase English letters (26 slots)
        p_count = [0] * 26
        s_count = [0] * 26

        # Populate target p_count map and initialize the first sliding window frame in s_count
        for i in range(p_len):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        # If the initial window frame is a perfect match
        if s_count == p_count:
            result.append(0)

        # Slide the window frame across string s starting from index p_len
        for i in range(p_len, s_len):
            # 1. Add the incoming right character to the current window
            s_count[ord(s[i]) - ord('a')] += 1
            # 2. Evict the outgoing leftmost character from the window frame boundary
            s_count[ord(s[i - p_len]) - ord('a')] -= 1

            # 3. Compare current window map status to target anagram layout layout
            if s_count == p_count:
                result.append(i - p_len + 1)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test Case matching Example 1
    string_s = "cbaebabacd"
    string_p = "abc"

    start_indices = sol.findAnagrams(string_s, string_p)
    print(f"S: '{string_s}', P: '{string_p}'")
    # S: 'cbaebabacd', P: 'abc'
    print(f"Anagram starting indices: {start_indices}")
    # Anagram starting indices: [0, 6]


# Time Complexity: O(N), where N is the length of string s. Populating the baseline counters takes O(M) time where M
# is the length of string p. The sliding window pass runs a single sweep across string s. At each position, updating
# individual letter indices takes constant O(1) operations, and comparing two fixed frequency arrays of size 26 takes
# exactly 26 operations, executing in strict linear runtime overall.
# Space Complexity: O(1) constant auxiliary space. The p_count and s_count tracking data arrays are bounded by
# a fixed maximum layout capacity of 26 integers matching the English alphabet character scale, making the extra
# memory independent of input size variations.
