# Task description:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.An Anagram is a
# word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
# letters exactly once (e.g., "eat", "tea", and "ate" are anagrams).

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Categorization by Sorted Key (using a Hash Map / Dictionary).
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Initialize a hash map where values default to an empty list
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the characters of the word to create a unique signature
            # e.g., "eat" -> ['a', 'e', 't'] -> "aet"
            sorted_key = "".join(sorted(word))

            # Append the original word to the corresponding anagram group
            anagram_map[sorted_key].append(word)

        # Return all categorized groups as a list of lists
        return list(anagram_map.values())


if __name__ == "__main__":
    # --- Example Usage ---
    sol = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(input_strs))
    # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]


# Complexity Analysis:
# Time Complexity: O(N*KlogK), where N is the number of strings in strs, and K is the maximum length of a string.
# We iterate through all N words, and sorting each word individually takes O(KlogK) time.
# Space Complexity: O(N*K) to store all the strings and their corresponding keys inside the hash map structure.
