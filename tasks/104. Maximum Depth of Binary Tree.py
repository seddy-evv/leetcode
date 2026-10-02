# Task description:
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Depth-First Search (DFS) via the Divide and Conquer strategy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: If the current node is empty, the depth is 0
        if not root:
            return 0

        # Divide: Recursively compute the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Conquer: The maximum depth is the max of the two subtrees plus 1 for the current node
        return max(left_depth, right_depth) + 1


from collections import deque


def build_tree(arr: list) -> TreeNode:
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
    # Represents tree matching Example 1: [3, 9, 20, None, None, 15, 7]
    tree_array = [3, 9, 20, None, None, 15, 7]
    root_node = build_tree(tree_array)

    sol = Solution()
    print(f"Maximum Depth of the Tree: {sol.maxDepth(root_node)}")
    # Maximum Depth of the Tree: 3


# Time Complexity: O(N), where N is the total number of nodes in the binary tree. The algorithm performs a complete
# post-order traversal, visiting each node exactly once.
# Space Complexity: O(H) auxiliary space, where H is the height of the tree. This space is consumed by the recursion
# call stack. In the worst case (a completely skewed linear tree), the space is O(N). In the best case (a completely
# balanced binary tree), the space complexity is O(log N).
