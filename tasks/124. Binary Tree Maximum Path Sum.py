# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
# connecting them. A node can only appear in the sequence at most once. Note that the path does not need to
# pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# Post-Order Depth-First Search (DFS) with Global Maximum Tracking, Tree task:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # Initialize global maximum with negative infinity
        self.max_sum = -float('inf')

        def get_max_gain(node: TreeNode | None) -> int:
            if not node:
                return 0

            # Recursively find the max path sum of left and right subtrees.
            # If the gain is negative, we drop it (cap at 0).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            # Check the sum of the path that splits/turns at the current node
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum if the current combined path is larger
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum single branch sum that can extend to the parent
            return node.val + max(left_gain, right_gain)

        # Start the bottom-up recursive scan
        get_max_gain(root)
        return self.max_sum


if __name__ == "__main__":
    # root = [-10, 9, 20, null, null, 15, 7]
    # Constructing the binary tree:
    #         -10
    #         /  \
    #        9    20
    #            /  \
    #           15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.maxPathSum(root))
    # 42


# Complexity Analysis:
# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The recursive DFS visits every
# node exactly once.
# Space Complexity: O(H), where H is the height of the tree. This is the memory occupied by the execution call stack.
# In the worst case (a completely unbalanced skewed tree), the space complexity is O(N); in a balanced tree, it is
# O(log N).
