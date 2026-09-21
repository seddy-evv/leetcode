# Task description:
# Reverse bits of a given 32 bits signed integer.

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110


# Constraints:
# 0 <= n <= 231 - 2
# n is even.

# Follow up: If this function is called many times, how would you optimize it?


# Bit Shifting and Masking Loop (Bitwise Reversal)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        # Unsigned 32-bit integer implies a fixed loop of 32 iterations
        for _ in range(32):
            # 1. Shift the result left to make room for the incoming bit
            result <<= 1

            # 2. Extract the rightmost bit of n and add it to the result
            result |= (n & 1)

            # 3. Shift n right to process the next bit in the sequence
            n >>= 1

        return result


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    # 43261596 in binary is 00000010100101000001111010011100
    print(sol.reverseBits(43261596))
    # Output: 964176192


# Time Complexity: O(1) constant time execution. Because the input constraint specifies a fixed length of a 32-bit
# integer, the loop runs exactly 32 times regardless of the value of n.
# Space Complexity: O(1) constant space. The calculation runs inline using only a single primitive integer variable
# (result) to build the bit layout.
