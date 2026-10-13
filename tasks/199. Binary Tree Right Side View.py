# Task description:
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Breadth-First Search (BFS) for Level-Order Traversal
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        # Traverse level by level
        while queue:
            level_length = len(queue)

            for i in range(level_length):
                curr = queue.popleft()

                # If it's the last node in the current level row, it's visible from the right side
                if i == level_length - 1:
                    result.append(curr.val)

                # Append left and right children to the queue for the next level sweep
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return result


if __name__ == "__main__":
    # Constructing a binary tree matching Example 1:
    #          1         <--- Visible: 1
    #        /   \
    #       2     3      <--- Visible: 3
    #        \     \
    #         5     4    <--- Visible: 4
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(2)
    tree_root.right = TreeNode(3)
    tree_root.left.right = TreeNode(5)
    tree_root.right.right = TreeNode(4)

    sol = Solution()
    visible_nodes = sol.rightSideView(tree_root)

    print(f"Right Side View: {visible_nodes}")
    # Output: [1, 3, 4]


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The level-order traversal visits
# every single node exactly once to build up the queue rows, running in linear time.
# Space Complexity: O(W) auxiliary space, where W is the maximum width of the tree. In the worst-case scenario
# (such as a fully balanced complete binary tree), the bottom queue layer can hold up to O(N/2) = O(N) leaf nodes
# concurrently.
