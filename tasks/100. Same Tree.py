# Task description:
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Recursive Depth-First Search (DFS) Traversal.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base case 1: Both nodes are null, so they are structurally identical
        if not p and not q:
            return True

        # Base case 2: One node is null and the other is not, or their values mismatch
        if not p or not q or p.val != q.val:
            return False

        # Recursively check if the left subtrees and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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


if __name__ == "__main__":
    sol = Solution()

    # Constructing trees for Example 1: p =, q = [1, 2, 3]
    tree_p = build_tree_from_list([1, 2, 3])
    tree_q = build_tree_from_list([1, 2, 3])
    print(f"Are trees identical? {sol.isSameTree(tree_p, tree_q)}")
    # Output: True

    # Constructing trees for Example 2: p =, q = [1, None, 2]
    tree_p2 = build_tree_from_list([1, 2])
    tree_q2 = build_tree_from_list([1, None, 2])
    print(f"Are trees identical? {sol.isSameTree(tree_p2, tree_q2)}")
    # Output: False


# Time Complexity: O(N), where N is the total number of nodes in the smaller of the two trees. The algorithm visits
# each node exactly once up until a mismatch or termination point is reached.
# • Space Complexity: O(H) auxiliary space, where H is the height of the tree. This space is consumed by the recursion
# call stack during traversal. In the worst case (a completely skewed linear tree), the space is O(N). In the best
# case (a completely balanced binary tree), the space complexity scales down to O(log N).
