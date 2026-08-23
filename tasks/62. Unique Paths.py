# Task description:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
# or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
# bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 10**9

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Constraints:
# 1 <= m, n <= 100

# Dynamic Programming (Space-Optimized Tabulation)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D DP array representing a single row.
        # There is exactly 1 way to reach any cell in the first row (by moving right).
        row = [1] * n

        # Iterate through the remaining m - 1 rows
        for r in range(1, m):
            # The first cell of any row always has exactly 1 way (by moving straight down)
            for c in range(1, n):
                # New value = paths from top (current row[c]) + paths from left (row[c-1])
                row[c] = row[c] + row[c - 1]

        return row[-1]


if __name__ == "__main__":
    m = 3
    n = 7
    sol = Solution()
    res = sol.uniquePaths(m, n)
    print(res)
    # 28

# Complexity Analysis:
# Time Complexity: O(m x n). We use a nested loop that iterates through every cell of the implicit
# grid exactly once.
# Space Complexity: O(n). Instead of maintaining an m × n matrix, we reuse a single 1D array of size n representing
# the current row.
