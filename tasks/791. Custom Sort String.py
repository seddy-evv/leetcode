# Task description:
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order
# previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
# occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example 1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also
# valid outputs.

# Example 2:
# Input: order = "bcafg", s = "abcd"
# Output: "bcad"
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character
# "d" in s does not appear in order, so its position is flexible.
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can
# be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements
# like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

# Constraints:
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.


#  Frequency Counting with Bucket Generation (Custom Hash Map Alignment).
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Count the frequency of each character in s
        s_counts = Counter(s)
        result = []

        # Step 2: Append characters in the sequence defined by order
        for char in order:
            if char in s_counts:
                result.append(char * s_counts[char])
                # Delete the key so we know it has been processed
                del s_counts[char]

        # Step 3: Append all remaining characters that were not present in order
        for char, count in s_counts.items():
            result.append(char * count)

        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcd"))
    # Output: "cbad" (or variations ending with d)


# Time Complexity: O(N + M), where N is the length of string s and M is the length of string order. Creating
# the frequency map takes O(N) time. Iterating through order takes O(M) time, and appending the remaining characters
# takes at most O(N) operations. This performs significantly faster than standard sorting O(NlogN).
# Space Complexity: O(N) auxiliary space. The Counter map holds at most the unique characters of s (bounded by a
# maximum of 26 keys if inputs are restricted to lowercase English letters). The result list stores N total characters
# before the final string conversion.
