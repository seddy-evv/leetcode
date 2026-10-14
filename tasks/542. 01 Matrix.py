# Task description:
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two cells sharing a common edge is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.


# Multi-Source Breadth-First Search (BFS).
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat or not mat[0]:
            return mat

        m, n = len(mat), len(mat[0])
        queue = deque()

        # Step 1: Initialize the queue with all '0' coordinates
        # and mark '1' cells as unvisited using infinity.
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')

        # Step 2: Perform Multi-Source BFS
        while queue:
            r, c = queue.popleft()

            # Explore 4 neighboring directions (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # If the neighbor is within bounds and finding a shorter path is possible
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat


if __name__ == "__main__":
    sol = Solution()

    # Test case matching Example 2
    matrix_input = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    result = sol.updateMatrix(matrix_input)
    print("Nearest distance matrix:")
    for row in result:
        print(row)

    # Output:
    # [0, 0, 0]
    # [0, 1, 0]
    # [1, 2, 1]


# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns. The multi-source approach
# ensures each grid cell is added to the queue and processed exactly once.
# Space Complexity: O(M*N) auxiliary space. The queue stores coordinate pairs and can contain up to O(M*N) nodes
# concurrently at its widest exploration boundary. Matrix tracking calculations are updated directly in-place,
# eliminating extra space overhead.
