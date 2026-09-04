# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: 6
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

# Example 2:
# Input: chars = ["a"]
# Output: 1
# Explanation: The only group is "a", which remains uncompressed since it is a single character.
# After modifying the input array in-place, the first character of chars should be ["a"].

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: 4
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
# After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].

# Constraints:
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


# Two Pointers Technique
class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        anchor = 0

        for read, char in enumerate(chars):
            # Check if we reached the end of the array or the next character is different
            if read + 1 == len(chars) or chars[read + 1] != char:
                # 1. Write the character
                chars[write] = chars[anchor]
                write += 1

                # 2. Write the count if the group length is greater than 1
                count = read - anchor + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                # Move the anchor to the next group's starting position
                anchor = read + 1

        return write


if __name__ == "__main__":

    sol = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    res = sol.compress(chars)
    print(res, chars[:res])
    # 6 ['a', '2', 'b', '2', 'c', '3']
    chars1 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    res = sol.compress(chars1)
    print(res, chars1[:res])
    # 4 ['a', 'b', '1', '2']


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the chars array. The read pointer traverses the array
# exactly once, and digits of the count are written in a small constant number of steps (since the maximum length of
# a string on LeetCode is small).
# Space Complexity: O(1) auxiliary space. The modification is done entirely in-place inside the input array, using
# only a few primitive integer pointer variables.
