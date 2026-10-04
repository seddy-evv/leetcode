# Task description:
# iven two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
# is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


# Divide and Conquer via Hash Map-Optimized Boundary Traversal.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # Map element values to their corresponding index in the inorder array.
        # This provides O(1) lookups to split the tree into subtrees instantly.
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Use an iterator over preorder to track the current root element cleanly
        preorder_iter = iter(preorder)

        def helper(left_bound: int, right_bound: int) -> TreeNode:
            # Base case: if boundaries cross, the current subtree is empty
            if left_bound > right_bound:
                return None

            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            # Find the split index in the inorder array
            split_idx = inorder_map[root_val]

            # Recursively build the left and right subtrees.
            # Elements to the left of split_idx belong to the left subtree.
            root.left = helper(left_bound, split_idx - 1)
            # Elements to the right of split_idx belong to the right subtree.
            root.right = helper(split_idx + 1, right_bound)

            return root

        return helper(0, len(inorder) - 1)


from collections import deque


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
    preorder_input = [3, 9, 20, 15, 7]
    inorder_input = [9, 3, 15, 20, 7]

    sol = Solution()
    reconstructed_tree_root = sol.buildTree(preorder_input, inorder_input)

    print(f"Reconstructed Tree (Level Order): {print_level_order(reconstructed_tree_root)}")
    # Output: [3, 9, 20, None, None, 15, 7]


# Time Complexity: O(N), where N is the total number of nodes in the tree. Building the inorder_map takes linear 
# O(N) time. During reconstruction, the helper function processes each node exactly once, looking up its split position 
# in constant O(1) time.
# Space Complexity: O(N) auxiliary space. This memory footprint holds the inorder_map which contains all N node 
# coordinates. Additionally, the call stack under deep recursion takes up to O(H) space where H is the height of the 
# tree (scaling up to O(N) in a completely skewed bamboo tree, or down to O(log N) for a fully balanced structure).
