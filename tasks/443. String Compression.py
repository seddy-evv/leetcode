# Given an array of characters chars, compress it using the following algorithm:
# 1. Begin with an empty string s.
# 2. For each group of consecutive repeating characters in chars:
#  1. If the group's length is 1, append the character to s.
#  2. Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately. Instead, you must modify the input array chars in-place
# so that the first k characters of the array contain the compressed string. Return the new length k of the array.
# You must write an algorithm that uses only O(1) extra space.

# Example 1:
# Input: chars = ["a","a","b","b","b","c"]
# Output: Return 5, and the first 5 characters of the input array should be: ["a","2","b","3","c"]

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]
# (Lengths greater than 9 are split into multiple characters).


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
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(sol.compress(chars), chars)
    # 4['a', 'b', '1', '2', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    chars1 = ["a", "a", "b", "b", "b", "c"]
    print(sol.compress(chars1), chars1)
    # 5['a', '2', 'b', '3', 'c', 'c']


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the chars array. The read pointer traverses the array
# exactly once, and digits of the count are written in a small constant number of steps (since the maximum length of
# a string on LeetCode is small).
# Space Complexity: O(1) auxiliary space. The modification is done entirely in-place inside the input array, using 
# only a few primitive integer pointer variables.
