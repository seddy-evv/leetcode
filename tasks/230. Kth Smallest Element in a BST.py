# Task description:
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values
# of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the
# kth smallest frequently, how would you optimize?


# In-Order Depth-First Search (DFS) with Early Stopping.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        # Iterative In-Order Traversal
        while curr or stack:
            # 1. Travel as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. Process the current node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val  # Early stopping when kth smallest is reached

            # 3. Turn to the right subtree
            curr = curr.right


if __name__ == "__main__":
    # Constructing Tree from Example 1:
    #        3
    #       / \
    #      1   4
    #       \
    #        2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    sol = Solution()

    k_val = 1
    result = sol.kthSmallest(root, k=k_val)
    print(f"The {k_val}st smallest element is: {result}")  # Output: 1

    k_val_2 = 3
    result_2 = sol.kthSmallest(root, k=k_val_2)
    print(f"The {k_val_2}rd smallest element is: {result_2}")  # Output: 3


# Time Complexity: O(H + K), where H is the height of the tree and K is the target rank. The algorithm traverses
# down to the leftmost leaf node in O(H) time, then processes exactly K elements. In the worst case of a skewed linear
# tree, this can be O(N). On average for a balanced tree, it operates in O(logN + K).
# Space Complexity: O(H) auxiliary space, where H is the height of the tree. The explicit tracking stack stores at 
# most the nodes along the deepest path from the root to a leaf node. This scales up to O(N) in a fully skewed tree 
# and drops to O(log N) for a well-balanced tree layout.
