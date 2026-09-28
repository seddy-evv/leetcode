# Task description:
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# Matrix Transposition followed by Row Reversal
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    # Instantiate the solution
    sol = Solution()

    # Example 1: 3x3 Matrix
    matrix1 = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    print("Result 1 (3x3):")
    for row in matrix1:
        print(row)
    # Output:
    # [7, 4, 1]
    # [8, 5, 2]
    # [9, 6, 3]

    # Example 2: 4x4 Matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12 ,16]]
    sol.rotate(matrix2)
    print("\nResult 2 (4x4):")
    for row in matrix2:
        print(row)
    # Output:
    # [15, 13, 2, 5]
    # [14, 3, 4, 1]
    # [12, 6, 8, 9]
    # [16, 7, 10, 11]


# Time Complexity: O(N^2), where N is the side length of the matrix (making N² the total number of cells).
# The transposition step visits roughly half the cells, and the reversal step visits every row once, reversing its N
# elements. Thus, the total work scales linearly with the number of cells in the matrix.
# Space Complexity: O(1). The algorithm restructures and updates values entirely in-place utilizing Python's tuple
# unpacking for swaps. No extra matrices, lists, or structural copies are allocated in memory.
