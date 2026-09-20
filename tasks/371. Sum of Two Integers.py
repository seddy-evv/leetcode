# Task description:
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

# Constraints:
# -1000 <= a, b <= 1000


# Bit Manipulation (Half Adder Simulation).
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit Mask to handle Python's arbitrary precision integers
        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate sum without carry, bound to 32 bits
            temp_sum = (a ^ b) & mask
            # Calculate carry and shift it left by 1, bound to 32 bits
            carry = ((a & b) << 1) & mask

            a = temp_sum
            b = carry

        # If the result 'a' represents a negative 32-bit number,
        # convert it back to a standard negative Python integer
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 2))
    # Output: 3
    print(sol.getSum(-2, 3))
    # Output: 1

# Time Complexity: O(1) constant execution time. Since the problem limits inputs to standard 32-bit integers,
# the loop can run at most 32 times (the number of bits) before the carry completely shifts out of bounds and
# becomes zero.
# Space Complexity: O(1) auxiliary space. We only use primitive local integer variables (mask, temp_sum, carry)
# to manipulate bits directly.
