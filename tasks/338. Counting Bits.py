# Task description:
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Constraints:
# 0 <= n <= 105
# Follow up:
# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and
# possibly in a single pass?


# Dynamic Programming with Least Significant Bit (LSB) Offset / Bit-Shift Relocation.
class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize a DP table of size n + 1 filled with zeros
        # Base case: ans[0] is already correctly set to 0
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # i >> 1 drops the lowest bit (same as i // 2)
            # i & 1 extracts the lowest bit (1 if odd, 0 if even)
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    # Output: [0, 1, 1]
    print(sol.countBits(5))
    # Output: [0, 1, 1, 2, 1, 2]


# Time Complexity: O(N), where N is the input integer n. We loop from 1 to N exactly once, performing constant
# time O(1) bitwise transitions at each index by utilizing previous calculations.
# Space Complexity: O(1) auxiliary space. The ans array is the required return format specified by the task
# definition and does not count toward extra space. No additional tracking arrays or sets are created.


