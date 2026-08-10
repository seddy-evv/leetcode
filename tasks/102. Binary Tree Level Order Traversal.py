# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
# level by level).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []


# Breadth-First Search (BFS) using a Queue, Tree task:
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        result = []
        # Initialize a double-ended queue with the root node
        queue = deque([root])

        while queue:
            # The number of elements currently in the queue represents the width of the current level
            level_size = len(queue)
            current_level_values = []

            # Process all nodes belonging strictly to this level
            for _ in range(level_size):
                curr_node = queue.popleft()
                current_level_values.append(curr_node.val)

                # Push children to the queue to be processed on the subsequent level loop
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            # Add the completed level list to our final results matrix
            result.append(current_level_values)

        return result


if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]
    # Constructing the binary tree:
    #        3
    #       / \
    #      9  20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.levelOrder(root))
    # [[3], [9, 20], [15, 7]]


# Complexity Analysis:
# Time Complexity: O(N), where N is the total number of nodes in the binary tree. We visit and extract every single
# node from the queue exactly once.
# Space Complexity: O(N) auxiliary space. In the worst-case scenario (a perfectly balanced complete
# binary tree), the bottom-most leaf level will contain up to N/2 nodes, which means the queue must be
# able to hold up to half of the tree's total nodes simultaneously.
