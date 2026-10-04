# Task description:
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once in a word.


# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.


# Backtracking with a Trie (Prefix Tree) and In-place Optimization (Pruning).
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie structure from the word bank
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w  # Store the actual word at the leaf node

        m, n = len(board), len(board[0])
        result = []

        # Step 2: Backtracking function via Depth-First Search
        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # If a word is matched, add it to our output list
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Deduplicate to avoid adding the same word twice

            # Mark the current board tile as visited
            board[r][c] = "#"

            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Revert the board tile back to its original letter state (Backtrack)
            board[r][c] = char

            # Optimization Optimization (Pruning): Remove leaf nodes to save time on subsequent paths
            if not curr_node.children:
                del parent_node.children[char]

        # Step 3: Run the search algorithm across every cell coordinate
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result


if __name__ == "__main__":
    test_board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    test_words = ["oath", "pea", "eat", "rain"]

    sol = Solution()
    matched_words = sol.findWords(test_board, test_words)

    print(f"Words found on the board: {matched_words}")
    # Output: ['oath', 'eat']


# Time Complexity: O(W*L + M*N*4*3^(L-1)), where:
# 	• W is the total number of items in words and L is the maximum length of a word. Building the initial Trie
# 	structure takes O(W*L) time.
# 	• M × N is the matrix grid layout size. At each grid starting position, the maximum deep recursion steps check up 
# 	to 4 neighbors on the first branch and up to 3 neighbors for all subsequent letters (since we cannot travel 
# 	backward onto the current path), bounding the traversal runtime.
# • Space Complexity: O(W*L) auxiliary space required to instantiate the TrieNode instances to store the unique 
# string combinations. The execution recursion stack allocation depth is strictly bounded by the maximum word length L.
