# Task description:
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
# return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only
# happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


# Multi-Source Breadth-First Search (BFS).
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes_elapsed = 0

        # Step 1: Scan the grid to count fresh oranges and enqueue all initial rotten ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges to begin with, 0 minutes are needed
        if fresh_oranges == 0:
            return 0

        # Step 2: Multi-source BFS layer-by-layer traversal
        while queue and fresh_oranges > 0:
            minutes_elapsed += 1
            # Process all rotten oranges at the current minute level
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Explore 4 neighboring directions (Up, Down, Left, Right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    # If neighbor is valid and contains a fresh orange, infect it
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))

        # Step 3: If fresh oranges still remain, it's impossible to rot them all
        return minutes_elapsed if fresh_oranges == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 1
    test_grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = sol.orangesRotting(test_grid)
    print(f"Minimum minutes to rot all oranges: {result}")
    # Output: 4


# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns in the grid. The initial
# setup scans all cells once. During the multi-source BFS traversal, each grid cell is entered and processed inside
# the queue at most once.
# • Space Complexity: O(M*N) auxiliary space. In the worst-case scenario, the queue tracks up to O(M*N) nodes
# concurrently if a large portion of the grid becomes rotten during a single phase. Modifications are applied directly
# onto the input array, avoiding extra matrix layer storage overhead.
