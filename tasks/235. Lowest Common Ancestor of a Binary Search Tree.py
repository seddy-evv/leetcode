# Task description:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


# Iterative BST Property Traversal (Binary Search-Style Subtree Partitioning).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # If both target nodes are greater than current node, move right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both target nodes are smaller than current node, move left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or matching node), which is the LCA
            else:
                return curr


if __name__ == "__main__":
    # Constructing BST from Example 1:
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    # Isolate targets
    p_node = root.left  # Node 2
    q_node = root.right  # Node 8
    q_node_2 = root.left.right  # Node 4

    sol = Solution()

    # Test Case 1
    result1 = sol.lowestCommonAncestor(root, p_node, q_node)
    print(f"LCA of {p_node.val} and {q_node.val} is: {result1.val}")  # Output: 6

    # Test Case 2
    result2 = sol.lowestCommonAncestor(root, p_node, q_node_2)
    print(f"LCA of {p_node.val} and {q_node_2.val} is: {result2.val}")  # Output: 2


# Time Complexity: O(H), where H is the height of the binary search tree. At each step, the algorithm discards one 
# entire side of the tree. In the average case of a balanced BST, this translates to a highly efficient O(log N). 
# In the worst case of a completely skewed linear tree, it can step through all elements, resulting in O(N).
# • Space Complexity: O(1) auxiliary space. Unlike the general binary tree version (LeetCode #236) which relies on 
# recursive stacks, this iterative path optimization runs inline by utilizing simple pointer updates, keeping memory 
# completely constant.
