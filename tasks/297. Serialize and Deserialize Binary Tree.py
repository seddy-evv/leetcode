# Task description:
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
# the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
# need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000


# Pre-Order Depth-First Search (DFS) Traversal with String Tokenization.
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        vals = []

        def rserialize(node):
            if not node:
                vals.append("#")
                return
            # Pre-order: Root -> Left -> Right
            vals.append(str(node.val))
            rserialize(node.left)
            rserialize(node.right)

        rserialize(root)
        # Combine all tokens using a delimiter character
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        # Convert the serialized string back into an iterable collection of string tokens
        tokens = data.split(",")
        # Use an iterator to keep track of our position inside the recursive calls cleanly
        token_iter = iter(tokens)

        def rdeserialize():
            val = next(token_iter)
            if val == "#":
                return None

            # Create the current node and recursively assign left and right children
            node = TreeNode(int(val))
            node.left = rdeserialize()
            node.right = rdeserialize()
            return node

        return rdeserialize()


if __name__ == "__main__":
    # Setup manual Binary Tree matching Example 1:
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    # 1. Run Serialization
    serialized_str = codec.serialize(root)
    print(f"Serialized String Output:  '{serialized_str}'")
    # Expected Output: '1,2,#,#,3,4,#,#,5,#,#'

    # 2. Run Deserialization
    deserialized_root = codec.deserialize(serialized_str)

    # 3. Simple Verification Check
    print(f"Deserialized Root Value:     {deserialized_root.val}")
    # Output: 1
    print(f"Deserialized Left Child:     {deserialized_root.left.val}")
    # Output: 2
    print(f"Deserialized Right Child:    {deserialized_root.right.val}")
    # Output: 3


# Time Complexity: O(N) for both serialize and decode routines, where N is the total number of nodes in the binary tree. 
# Every single node and null marker is visited exactly once to serialize or rebuild the structure.
# Space Complexity: O(N) auxiliary space. During encoding, the vals list keeps track of string nodes up to length N. 
# During decoding, the split collection tokens holds array pointers up to size N. Additionally, the execution stack 
# footprints under deep recursion take up to \(\mathcal{O}(H)\) memory where H is the max tree height.
