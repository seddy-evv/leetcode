# Task description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


# Sorting-Based Extrema Comparison approach
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Sort the strings lexicographically (alphabetically)
        strs.sort()

        # Get the first and last strings after sorting
        first = strs[0]
        last = strs[-1]

        # Compare characters of the first and last strings
        prefix_len = 0
        min_len = min(len(first), len(last))

        while prefix_len < min_len and first[prefix_len] == last[prefix_len]:
            prefix_len += 1

        # Return the matching common substring
        return first[:prefix_len]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    # Output: "fl"


# Complexity Analysis:
# Time Complexity: O(M*NlogN) in the worst case, where N is the number of strings and M is
# the maximum length of a string (due to string comparisons during sorting). However, practically speaking, sorting
# only inspects characters until a difference is found, making this approach extremely fast and concise.
# Space Complexity: O(1) or O(N) depending on the sorting implementation memory profile.
# Python's Timsort uses linear extra space for tracking arrays. No extra collections are created by the algorithm itself.
