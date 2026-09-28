# Task description:
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


# In-Place Matrix Hashing (Using First Row and First Column as Flags)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False

        # Step 1: Check if the first row or first column has any zeros
        for c in range(COLS):
            if matrix[0][c] == 0:
                row_zero = True
                break

        for r in range(ROWS):
            if matrix[r][0] == 0:
                col_zero = True
                break

        # Step 2: Use the first row and column to flag zeros for inner cells
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 3: Zero out the inner cells based on the flags
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 4: Zero out the first row if needed
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        # Step 5: Zero out the first column if needed
        if col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0


if __name__ == "__main__":
    # Instantiate the solution
    sol = Solution()

    # Example 1: 3x3 Matrix with one zero
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix1)
    print("Result 1:")
    for row in matrix1:
        print(row)
    # Output:
    # [1, 0, 1]
    # [0, 0, 0]
    # [1, 0, 1]

    # Example 2: 3x4 Matrix with multiple zeros
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix2)
    print("\nResult 2:")
    for row in matrix2:
        print(row)
    # Output:
    # [0, 0, 0, 0]
    # [0, 4, 5, 0]
    # [0, 3, 1, 0]


# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns. The algorithm passes over
# the matrix a constant number of times (first to establish flags, second to mark indices, and third to distribute
# zeros). This yields an optimal linear time complexity relative to the total number of elements.
# Space Complexity: O(1). No supplementary array structures or hash sets are allocated. The state markers are stored
# completely within the given input arrays, matching the optimal constraint condition of strictly constant auxiliary
# space.
