# Task Description
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.

# Examples
# Example 1:
# Input:
grid1 = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]
# Output: 1

# Example 2:
# Input:
grid2 = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300grid
# [i][j] is '0' or '1'.


# DFS Approach:

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r: int, c: int):
        # Base case: if out of bounds or current cell is water ('0'), stop recursion
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Sink the land: mark current cell as '0' to avoid visiting it again
        grid[r][c] = '0'

        # Recursively visit all 4 adjacent neighbors (Up, Down, Left, Right)
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Traverse every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find unvisited land ('1'), we found a new island
            if grid[r][c] == '1':
                island_count += 1
                # Use DFS to sink the entire island
                dfs(r, c)

    return island_count


if __name__ == "__main__":
    print(numIslands(grid1))
    # 1

# Key Logic & Mechanism
# - Linear Scan: We scan the 2D grid row by row. When we encounter a '1', it triggers a new island count and initiates
#   a DFS traversal.
# - Island "Sinking" (In-place Tracking): To avoid using O(MxN) extra space for a visited set,
#   we change the visited '1's directly to '0's during the DFS. This prevents infinite loops.
# - 4-Way Exploration: From the current piece of land, the DFS branches out recursively in four directions
#   (up, down, left, right) to destroy the rest of the connected island before returning to the main loops.

# Complexity Analysis
# Time Complexity: O(MxN) where M is the number of rows and N is the number of columns. Every cell is visited at most
# a few times.
# Space Complexity: O(MxN) in the worst-case scenario where the entire grid is filled with land.
# The recursion stack can grow to the size of the grid.
