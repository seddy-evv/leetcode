# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive
# identical characters with the concatenation of the length of the group followed by the character itself.
# For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5"
# with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:
# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

# Constraints:

# 1 <= n <= 30


# Linear Scan with String Accumulation (Simulation of Run-Length Encoding)
class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"

        # Generate the sequence iteratively up to the n-th step
        for _ in range(n - 1):
            next_string_chunks = []
            count = 1

            # Scan the current string to perform Run-Length Encoding
            for i in range(1, len(current_str)):
                if current_str[i] == current_str[i - 1]:
                    count += 1
                else:
                    # Append the count of digits and the digit itself
                    next_string_chunks.append(str(count))
                    next_string_chunks.append(current_str[i - 1])
                    count = 1  # Reset count for the new digit

            # Append the very last group of digits after the loop ends
            next_string_chunks.append(str(count))
            next_string_chunks.append(current_str[-1])

            # Update current_str to be the newly generated sequence
            current_str = "".join(next_string_chunks)

        return current_str


if __name__ == "__main__":

    sol = Solution()
    chars = "aabbbc"
    print(sol.countAndSay(4))
    # 1211


# Complexity Analysis:
# Time Complexity: O(2^m) in the absolute worst-case bounding scenario, where m is proportional to n.
# In practice, the length of the string grows roughly by a factor of 1.3 to 1.4 each iteration, making it highly
# optimized for small values of n (usually up to n=30 on LeetCode).
# Space Complexity: O(k) where k is the maximum length of the string generated during the sequence transition. We use
# an array (next_string_chunks) to build up the string elements before joining them, which protects against the memory
# overhead of cumulative string immutability in Python.
