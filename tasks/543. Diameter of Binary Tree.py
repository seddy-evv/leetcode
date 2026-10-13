# Task description:
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or
# may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


# Bottom-Up Depth-First Search (DFS) via Post-Order Traversal.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def calculate_depth(node: TreeNode) -> int:
            # Base case: An empty node contributes 0 to the depth
            if not node:
                return 0

            # 1. Recursively find the depth of left and right subtrees
            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)

            # 2. Update the global max diameter if the path through the current node is longer
            current_diameter = left_depth + right_depth
            self.max_diameter = max(self.max_diameter, current_diameter)

            # 3. Return the max depth of the current subtree back up to the parent
            return max(left_depth, right_depth) + 1

        calculate_depth(root)
        return self.max_diameter


if __name__ == "__main__":
    # Constructing a binary tree matching Example 1:
    #          1
    #         / \
    #        2   3
    #       / \
    #      4   5
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(2)
    tree_root.right = TreeNode(3)
    tree_root.left.left = TreeNode(4)
    tree_root.left.right = TreeNode(5)

    sol = Solution()
    result = sol.diameterOfBinaryTree(tree_root)

    print(f"The diameter of the binary tree is: {result}")
    # Output: 3


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The bottom-up method ensures that
# we visit each node exactly once to compute its depth, matching the optimal execution time constraint.
# • Space Complexity: O(H) auxiliary space, where H is the maximum height of the tree. This memory footprint
# corresponds directly to the maximum allocation depth of the recursive call stack. In the worst-case scenario of
# a completely skewed tree (bamboo tree), it can scale to O(N), while in a perfectly balanced binary tree, it limits
# itself to a clean O(log N).
