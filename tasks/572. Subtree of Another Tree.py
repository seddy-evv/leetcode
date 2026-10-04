# Task description:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.


# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104


# Recursive Depth-First Search (DFS) with Structural Tree Matching (Isomorphism Check)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Base Cases
        if not subRoot:
            return True  # An empty tree is always a subtree
        if not root:
            return False  # If root is empty but subRoot isn't, it cannot be a subtree

        # If the trees starting at current nodes are identical, return True
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, recursively check if subRoot is a subtree of the left or right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Helper function to check if two trees are structurally identical (LeetCode #100)."""
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Constructing main tree (root) matching Example 1:
    #        3
    #       / \
    #      4   5
    #     / \
    #    1   2
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    # Constructing sub-tree (subRoot):
    #      4
    #     / \
    #    1   2
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    sol = Solution()

    # Run the subtree verification check
    result = sol.isSubtree(root, subRoot)
    print(f"Is subRoot a valid subtree of root? {result}")
    # Output: True


# Time Complexity: O(M*N) in the worst case, where M is the number of nodes in the root tree and N is the number
# of nodes in the subRoot tree. In the worst-case scenario (such as a tree where all nodes have the same value),
# isSameTree can be invoked for every node in root.
# • Space Complexity: O(H_root) auxiliary space, where H_root is the height of the main tree. This memory
# footprint represents the maximum depth of the recursive call stack. In a completely skewed tree, it can scale
# to O(M), whereas in a balanced binary tree, it limits itself to a clean O(log M).
