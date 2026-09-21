# Task description:
# Given a positive integer n, write a function that returns the number of set bits in its binary representation
# (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:
# 1 <= n <= 231 - 1
# Follow up: If this function is called many times, how would you optimize it?


# Brian Kernighan’s Algorithm (Bitwise Set-Bit Clearing).
class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits_count = 0

        while n > 0:
            # Bitwise trick: clears the lowest set bit (rightmost 1-bit)
            n = n & (n - 1)
            # Increment the counter for each cleared 1-bit
            set_bits_count += 1

        return set_bits_count


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))
    # Output: 3 (since 11 is 1011 in binary)
    print(sol.hammingWeight(128))
    # Output: 1 (since 128 is 10000000 in binary)


# Time Complexity: O(K) where K is the exact number of set bits (1s) present in the number. In a 32-bit integer,
# this loop runs at most 32 times, but on average much fewer, making it strictly superior to checking every bit
# sequentially.
# Space Complexity: O(1) auxiliary space, as only a single local tracking scalar integer (set_bits_count) is used in memory.

