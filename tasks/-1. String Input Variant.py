# Given an input string s, compress it using Run-Length Encoding (RLE). For every consecutive sequence of repeating
# characters, replace them with the character followed by the number of repetitions. If a character appears only
# once, keep it as is (or append 1 depending on the exact variation, but keeping just the character is standard).

# Example 1:
# Input: s = "aabbbc"
# Output: "a2b3c"

# Example 2:
# Input: s = "abc"
# Output: "abc"

# Example 3:
# Input: s = "aaaaaaaaaa"
# Output: "a10"


# Linear Scan with String Builder / String Accumulation
class Solution:
    def encode_string(self, s: str) -> str:
        if not s:
            return ""

        result_chunks = []
        count = 1

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                # Append the character
                result_chunks.append(s[i - 1])
                # Append count only if it's greater than 1
                if count > 1:
                    result_chunks.append(str(count))
                # Reset counter for the new character group
                count = 1

        # Handle the very last group of characters after the loop finishes
        result_chunks.append(s[-1])
        if count > 1:
            result_chunks.append(str(count))

        # Join the list into a single final string efficiently
        return "".join(result_chunks)


if __name__ == "__main__":

    sol = Solution()
    chars = "aabbbc"
    print(sol.encode_string(chars))
    # a2b3c
    chars1 = "abc"
    print(sol.encode_string(chars1))
    # abc


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the string s. We loop through the string exactly once. Appending
# to a list takes O(1) time, and "".join() takes O(n) time.
# Space Complexity: O(n) because we must store and return a brand-new compressed string.
