# Task description:
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# Layer-by-Layer Simulation via Boundary Traversal.
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        # Initialize the 4 boundaries of the matrix
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse from Left to Right along the current top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Contract the top boundary downward

            # 2. Traverse from Top to Bottom along the current right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Contract the right boundary leftward

            # Check if boundaries crossed after moving top and right pointers
            if top <= bottom:
                # 3. Traverse from Right to Left along the current bottom row
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Contract the bottom boundary upward

            if left <= right:
                # 4. Traverse from Bottom to Top along the current left column
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Contract the left boundary rightward

        return result


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(test_matrix))
    # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


# Time Complexity: O(MxN), where M is the number of rows and N is the number of columns. The simulation visits every
# single cell in the matrix exactly once to append it to the result array.
# Space Complexity: O(1) auxiliary space. If we exclude the memory space allocated to store the final result list,
# the pointer variables (top, bottom, left, right) consume strict constant storage in memory.
