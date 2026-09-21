# Task description:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Constraints:
# 1 <= n <= 45


# Dynamic Programming (Space-Optimized Tabulation), which structurally mirrors the Fibonacci Sequence Calculation.
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n

        # Track the number of ways to reach 1 step ago and 2 steps ago
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2

        for i in range(3, n + 1):
            # Total ways to reach the current step
            current = prev1 + prev2

            # Slide our state variables forward for the next iteration
            prev2 = prev1
            prev1 = current

        return prev1


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))
    # Output: 2
    print(sol.climbStairs(3))
    # Output: 3

# Time Complexity: O(N), where N is the target integer n. The algorithm executes a single sequential loop from 3 to n.
# Space Complexity: O(1) auxiliary space. By using only a few constant scalar variables (prev1, prev2, current)
# instead of an allocated array of size n + 1, memory usage remains completely independent of the size of n.
