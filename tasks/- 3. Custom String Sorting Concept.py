# To sort a string in O(n) time complexity, traditional comparison-based sorting algorithms (like QuickSort or
# MergeSort) cannot be used because they take (O(nlog n). Instead, we must use a non-comparison counting method.
# Task Description:
# Given a string s, sort its characters in ascending order based on their ASCII/Unicode values
# (or a fixed alphabet size) in O(n) time complexity and O(1) auxiliary space.


# Counting Sort (Frequency Map Method)
class Solution:
    def sortString(self, s: str) -> str:
        # Step 1: Count frequencies of each character
        # Since the alphabet size is fixed (e.g., 256 ASCII), this takes O(1) space
        char_counts = [0] * 256
        for char in s:
            char_counts[ord(char)] += 1

        # Step 2: Reconstruct the sorted string
        result = []
        for ascii_val in range(256):
            if char_counts[ascii_val] > 0:
                result.append(chr(ascii_val) * char_counts[ascii_val])

        return "".join(result)


if __name__ == "__main__":
    s = "cdab"
    sol = Solution()
    res = sol.sortString(s)
    print(res)
    # abcd

# Complexity Analysis:
# Time Complexity: O(n + K) where n is the length of the string and K is the alphabet size (256 for extended ASCII).
# Since K is constant, this simplifies to O(n).
# Space Complexity: O(1) auxiliary space because the size of the frequency array remains fixed at 256 regardless of
# the input string length.
