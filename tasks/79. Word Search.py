# Task description:
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?


# Backtracking via Depth-First Search (DFS)
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            # Base Case: If the entire word has been successfully matched
            if index == len(word):
                return True

            # Boundary and mismatch checks
            if (r < 0 or r >= m or c < 0 or c >= n or
                    board[r][c] != word[index]):
                return False

            # Step 1: Mark the cell as visited to prevent reuse in the current path
            temp = board[r][c]
            board[r][c] = "#"

            # Step 2: Explore all 4 adjacent directions (Up, Down, Left, Right)
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))

            # Step 3: Revert the cell back to its original state (Backtrack)
            board[r][c] = temp

            return found

        # Traverse every cell on the board to find a valid starting point
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    test_board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    print(sol.exist(test_board, "ABCCED"))  # Output: True
    print(sol.exist(test_board, "ABCB"))  # Output: False


# Time Complexity: (M*N*3^L), where M × N is the grid dimension size and L is the length of the target word. We check
# every starting cell in the grid, and from there we branch out in up to 3 directions at each letter step (4 directions
# initially, but we cannot step back onto the cell we just came from).
# Space Complexity: O(L) auxiliary space required due to the execution recursion stack limits, which can grow up to
# the depth of the total word length L. Modifying the board characters directly inline to store visited marks ensures
# a strict O(1) extra tracking matrix footprint.
