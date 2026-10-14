# Task description:
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value
# of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on
# the image starting from the pixel image[sr][sc].
#
# To perform a flood fill:
# 1. Begin with the starting pixel and change its color to color.
# 2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# 3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# 4. The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path
# of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation:
# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes
# are made to the image.

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n


# Depth-First Search (DFS) / Connected Component Traversal
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Store the baseline original color of the starting pixel
        start_color = image[sr][sc]

        # Edge case: If the starting pixel already matches the target color,
        # returning the image immediately prevents an infinite recursion loop.
        if start_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r: int, c: int):
            # Check boundary conditions and verify the current pixel matches the original starting color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return

            # Update the color of the current pixel
            image[r][c] = color

            # Recursively cascade the color fill 4-directionally (Up, Down, Left, Right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Begin traversal from the requested coordinate source
        dfs(sr, sc)
        return image


if __name__ == "__main__":
    sol = Solution()

    # Setup test matrix matching Example 1
    input_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    result = sol.floodFill(image=input_image, sr=1, sc=1, color=2)
    print("Modified Grid Matrix:")
    for row in result:
        print(row)
    # Output:
    # [2, 2, 2]
    # [2, 2, 0]
    # [2, 0, 1]


# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns in the grid image. In the
# worst-case scenario, the flood fill path encompasses every single coordinate node within the matrix exactly once.
# Space Complexity: O(M*N) auxiliary space. No additional allocation structural matrix layers are instantiated
# because the grid modifications occur directly in-place. However, the internal call stack depth during recursion
# scales up to O(M*N) in a completely uniform image fill.
