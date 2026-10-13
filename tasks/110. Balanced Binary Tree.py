# Task description:
# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Bottom-Up Depth-First Search (DFS) with Short-Circuit Pruning (also known as an Optimized Post-Order Traversal).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def check_height(node: TreeNode) -> int:
            # Base case: An empty tree has a height of 0 and is balanced
            if not node:
                return 0

            # 1. Recursively check the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced; propagate failure upward

            # 2. Recursively check the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced; propagate failure upward

            # 3. Check balance condition at the current node
            if abs(left_height - right_height) > 1:
                return -1  # Height difference exceeds 1; current node is unbalanced

            # If balanced, return the actual height of the current node
            return max(left_height, right_height) + 1

        # The tree is balanced if the helper function does not return our error sentinel -1
        return check_height(root) != -1


if __name__ == "__main__":
    # Constructing a Balanced Tree matching Example 1:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    balanced_tree = TreeNode(3)
    balanced_tree.left = TreeNode(9)
    balanced_tree.right = TreeNode(20)
    balanced_tree.right.left = TreeNode(15)
    balanced_tree.right.right = TreeNode(7)

    # Constructing an Unbalanced Tree matching Example 2:
    #         1
    #        / \
    #       2   2
    #      / \
    #     3   3
    #    / \
    #   4   4
    unbalanced_tree = TreeNode(1)
    unbalanced_tree.left = TreeNode(2)
    unbalanced_tree.right = TreeNode(2)
    unbalanced_tree.left.left = TreeNode(3)
    unbalanced_tree.left.right = TreeNode(3)
    unbalanced_tree.left.left.left = TreeNode(4)
    unbalanced_tree.left.left.right = TreeNode(4)

    sol = Solution()

    print(f"Is the first tree balanced?  {sol.isBalanced(balanced_tree)}")
    # Output: True
    print(f"Is the second tree balanced? {sol.isBalanced(unbalanced_tree)}")
    # Output: False


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The bottom-up method ensures that
# we visit each node at most once to calculate its height and verify subproblems, achieving pure linear execution
# performance.
# Space Complexity: O(H) auxiliary space, where H is the maximum height of the tree. This memory footprint corresponds
# directly to the maximum allocation depth of the recursive call stack. In the worst-case scenario of a completely
# skewed tree, it can scale to O(N), while in a perfectly balanced binary tree, it limits itself  to a clean O(log N).
