# Task description:
# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2.
# You may assume that multiplying the matrices is always valid (the number of columns in the first matrix is equal to
# the number of rows in the second matrix). A sparse matrix is a matrix where most of the elements are zero, meaning
# standard matrix multiplication can be highly optimized by skipping unnecessary math operations


# Sparse Matrix Multiplication via Coordinate Compression (or Non-Zero Element Skipping)
class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        m, k_dim = len(mat1), len(mat1[0])
        n = len(mat2[0])

        # Initialize result matrix with zeros
        result = [[0] * n for _ in range(m)]

        # Optimized Triple Loop (Row -> Common Dimension -> Column)
        for i in range(m):
            for k in range(k_dim):
                # If the element in the first matrix is 0, skipping avoids multiplication
                if mat1[i][k] != 0:
                    for j in range(n):
                        if mat2[k][j] != 0:
                            result[i][j] += mat1[i][k] * mat2[k][j]

        return result


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    sol = Solution()
    res = sol.multiply(A, B)
    print(res)
    # [[19, 22], [43, 50]]

# Complexity Analysis:
# Time Complexity: O(m*k*n) in the absolute worst case (if the matrices are entirely dense). However, for practical
# sparse inputs with non-zero counts of E₁ and E₂, the average running time reduces drastically towards
# O(m*k + E1*n/k), easily beating the raw brute-force dot product.
# Space Complexity: O(1) auxiliary space if we exclude the memory allocated to output the final m × n matrix.
