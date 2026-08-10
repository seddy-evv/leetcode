#  Problem DescriptionGiven a string s, find the first non-repeating character in it and return its index.
#  If it does not exist, return -1.
#  Example 1:
#  Input: s = "leetcode"
#  Output: 0
#  Explanation: The character 'l' at index 0 is the first character that does not repeat.

#  Example 2:
#  Input: s = "loveleetcode"
#  Output: 2
#  Explanation: The character 'v' at index 2 is the first character that does not repeat.

#  Example 3:
#  Input: s = "aabb"
#  Output: -1


# Frequency Map / Hash Map (Two-Pass Algorithm)
from collections import Counter


class Solution():
    # 1. Option using collections
    def find_first_unique_char_col(self, text: str) -> str or None:
        # Count frequencies of all characters
        char_counts = Counter(text)

        # Find the first character with a count of 1
        for char in text:
            if char_counts[char] == 1:
                return char

        return None  # Return None if all characters repeat

    # 2. Option using core Python structures (in Python 3.7+ dict preserving the order in which elements are added, but
    # this solution is version independent)
    def find_first_unique_char(self, text: str) -> str or None:
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1

        for char in text:
            if char_counts[char] == 1:
                return char

        return None


if __name__ == "__main__":

    sol = Solution()
    print(sol.find_first_unique_char_col("python"))  # Output: p
    print(sol.find_first_unique_char_col("swiss"))  # Output: w
    print(sol.find_first_unique_char_col("aabbcc"))  # Output: None

    print(sol.find_first_unique_char("python")) # Output: p
    print(sol.find_first_unique_char("swiss")) # Output: w
    print(sol.find_first_unique_char("ууууух")) # Output: x
    print(sol.find_first_unique_char("aabbcc")) # Output: None


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the string. The algorithm traverses the string at most twice.
# Space Complexity: O(K), where K is the number of unique characters stored in the dictionary (maximum of 256 for
# standard ASCII or bounded by the Unicode character set)
