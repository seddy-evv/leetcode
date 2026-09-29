# Task description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


# Frequency Counting via Hash Map (Frequency Counter Optimization).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths match differently, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Frequency tracking bucket dictionary
        count_map = {}

        # Populate count maps for character presence
        for i in range(len(s)):
            count_map[s[i]] = count_map.get(s[i], 0) + 1
            count_map[t[i]] = count_map.get(t[i], 0) - 1

        # If any bucket count is not exactly 0, strings do not match character metrics
        for count in count_map.values():
            if count != 0:
                return False

        return True


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    # Output: True
    print(sol.isAnagram("rat", "car"))
    # Output: False


# Time Complexity: O(N), where N is the length of string s (or t). We perform a single loop sequence across the string
# characters, looking up and updating dictionary keys in constant O(1) average time.
# Space Complexity: O(1) auxiliary space. Since the string elements belong to a fixed uppercase or lowercase English
# language character configuration, the hash map space is strictly bounded by a maximum capacity of 26 unique character
# slots.
