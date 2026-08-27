# Task description:
# LeetCode Pattern / LintCode #475: Binary Tree Maximum Path Sum II
# Given the root of a binary tree, find the maximum path sum where the path must start at the root node and travel
# downward to any node (it does not necessarily have to end at a leaf node). The path must contain at least one
# node (the root itself).
# This is a prominent follow-up or variant of the classic unconstrained LeetCode #124 (Binary Tree Maximum Path Sum).

# Example 1:
# Tree: [1, 2, 3]
# Output: 4
# Explanation: The optimal path starts at root 1 and goes to its right child 3 (1 + 3 = 4). A path like 2 -> 1 -> 3
# (summing to 6) is invalid here because it does not originate at the root.

# Example 2:
# Tree: [-10, 9, 20, null, null, 15, 7]
# Output: 25
# Explanation: The optimal path starting at the root is -10 -> 20 -> 15, which sums up to 25.


# Depth-First Search (DFS) via the Divide and Conquer strategy.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum2(self, root: TreeNode) -> int:
        # Base case: If the node is empty, it contributes 0 to the path sum
        if not root:
            return 0

        # Recursively find the max path sum starting from the left and right children
        left_sum = self.maxPathSum2(root.left)
        right_sum = self.maxPathSum2(root.right)

        # Since the path MUST include the root, we evaluate three choices:
        # 1. Take root only (if both children return negative path sums)
        # 2. Take root + maximum path from the left subtree
        # 3. Take root + maximum path from the right subtree
        # This can be written cleanly as: root.val + max(0, left_sum, right_sum)
        return root.val + max(0, max(left_sum, right_sum))


if __name__ == "__main__":
    # Constructing Tree from Example 2:
    #        -10
    #        /  \
    #       9    20
    #           /  \
    #          15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print("Maximum path sum from root:", sol.maxPathSum2(root))
    # Output: 25


# Complexity Analysis:
# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The algorithm visits each node
# exactly once to compute its localized maximum subtree choice.
# Space Complexity: O(H) auxiliary space, where H represents the height of the tree. This memory is allocated on
# the execution call stack due to recursion. In the worst case (a highly unbalanced, skewed tree), it can scale up
# to O(N), while in a fully balanced tree, it remains a clean O(log N).
