# Task description:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
# the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1


# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.


# Post-Order Depth-First Search (DFS) / Divide and Conquer.
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the current node is null, or matches either target node p or q,
        # return it immediately back up to the parent caller
        if not root or root == p or root == q:
            return root

        # Divide: Recursively search for p and q in both left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer / Combine:
        # If both left and right calls returned non-null values, it means p is on one side
        # and q is on the other side. Thus, the current root is their Lowest Common Ancestor.
        if left and right:
            return root

        # If only one side returned a non-null value, pass that result upward
        return left if left else right


if __name__ == "__main__":
    # Helper function to build a Binary Tree from LeetCode's level-order array representation
    def build_tree_from_list(arr: list) -> TreeNode:
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            curr = queue.popleft()

            # Build Left Child
            if i < len(arr) and arr[i] is not None:
                curr.left = TreeNode(arr[i])
                queue.append(curr.left)
            i += 1

            # Build Right Child
            if i < len(arr) and arr[i] is not None:
                curr.right = TreeNode(arr[i])
                queue.append(curr.right)
            i += 1

        return root


    # Helper function to find and return the actual TreeNode reference by value
    def find_node(root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        return find_node(root.left, val) or find_node(root.right, val)


    # --- Standard Test Case Setup ---

    # This matches LeetCode Example 1 and 2 tree structure:
    #          3
    #        /   \
    #       5     1
    #      / \   / \
    #     6   2 0   8
    #        / \
    #       7   4
    tree_array = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root_node = build_tree_from_list(tree_array)

    # Isolate the exact object references for target nodes p and q
    p_node = find_node(root_node, 5)
    q_node = find_node(root_node, 1)

    # --- Execution ---
    sol = Solution()
    lca_result = sol.lowestCommonAncestor(root_node, p_node, q_node)

    print(f"LCA of node {p_node.val} and node {q_node.val} is: {lca_result.val}")
    # LCA of node 5 and node 1 is: 3


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. In the worst-case scenario, the
# algorithm may need to traverse every single node to find both targets.
# Space Complexity: O(H) auxiliary space, where H is the height of the tree. This memory is allocated dynamically on
# the execution call stack due to recursion. In the worst case (a highly skewed tree), it can become O(N), while in
# a completely balanced tree, it remains a clean O(log N).
