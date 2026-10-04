# Task description:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Recursive Depth-First Search (DFS) with Boundary Range Validation.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node: TreeNode, low: float, high: float) -> bool:
            # Base case: An empty tree or leaf boundary node is always a valid BST
            if not node:
                return True

            # If the current node's value violates the valid range, it is not a valid BST
            if not (low < node.val < high):
                return False

            # Recursively validate subtrees with updated strict boundaries:
            # - Left child must be smaller than current node's value (updates high)
            # - Right child must be larger than current node's value (updates low)
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Initialize validation with infinity boundaries
        return validate(root, -float('inf'), float('inf'))


if __name__ == "__main__":
    # Setup manual Binary Tree matching Example 1: Valid BST
    #      2
    #     / \
    #    1   3
    valid_root = TreeNode(2)
    valid_root.left = TreeNode(1)
    valid_root.right = TreeNode(3)

    # Setup manual Binary Tree matching Example 2: Invalid BST
    #      5
    #     / \
    #    1   4
    #       / \
    #      3   6
    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(1)
    invalid_root.right = TreeNode(4)
    invalid_root.right.left = TreeNode(3)
    invalid_root.right.right = TreeNode(6)

    sol = Solution()

    print(f"Is the first tree a valid BST?  {sol.isValidBST(valid_root)}")
    # Output: True
    print(f"Is the second tree a valid BST? {sol.isValidBST(invalid_root)}")
    # Output: False


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The algorithm performs a full single 
# pass over the tree structure, evaluating each node's range correctness exactly once.
# Space Complexity: O(H) auxiliary space, where H is the height of the tree. This memory represents the execution 
# call stack depth during recursion. In the worst case (a highly unbalanced, skewed linear tree), the space scales 
# to O(N), whereas in a completely balanced binary tree, it limits itself to a clean O(log N).
