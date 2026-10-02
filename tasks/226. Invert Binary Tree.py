# Task description:
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Recursive Depth-First Search (DFS) / Post-Order Node Traversal.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base case: If the current node is null, there is nothing to invert
        if not root:
            return None

        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root node of the fully inverted tree
        return root


from collections import deque


def build_tree_from_list(arr: list) -> TreeNode:
    """Helper to convert LeetCode level-order array into a Binary Tree."""
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        curr = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1
    return root


def print_level_order(root: TreeNode) -> list:
    """Helper to output the tree back into a level-order list format."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
    # Trim trailing Nones to match clean LeetCode array representations
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()

    # Constructing tree for Example 1: [4, 2, 7, 1, 3, 6, 9]
    original_array = [4, 2, 7, 1, 3, 6, 9]
    tree_root = build_tree_from_list(original_array)

    print(f"Original tree: {print_level_order(tree_root)}")

    # Run the tree inversion algorithm
    inverted_root = sol.invertTree(tree_root)

    print(f"Inverted tree: {print_level_order(inverted_root)}")
    # Output: [4, 7, 2, 9, 6, 3, 1]


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The algorithm visits every single
# node exactly once to swap its pointer targets.
# • Space Complexity: O(H) auxiliary space, where H is the maximum height of the binary tree. This memory footprint
# represents the execution call stack bounds under deep recursion. In the worst-case scenario of a completely skewed
# tree, it can scale to O(N), while in a perfectly balanced binary tree layout, it stays at a clean O(log N).
