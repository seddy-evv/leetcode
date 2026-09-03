# Task description:
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any
# connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates
# that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree
# as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees,
# those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Constraints:
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.


# Topological Sort via Leaf Elimination (similar to Kahn's Algorithm, adapted for undirected acyclic graphs).
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Edge case: If there is only 1 node or 2 nodes, they are already the roots
        if n <= 2:
            return [i for i in range(n)]

        # Step 1: Build the adjacency list graph and track node degrees
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Step 2: Initialize a queue with all initial leaf nodes (degree == 1)
        leaves = deque()
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)

        # Step 3: Trim leaves level-by-level until 2 or fewer central nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()

                # The leaf only has one neighbor left in the set
                neighbor = graph[leaf].pop()
                # Remove the connection from the neighbor's side too
                graph[neighbor].remove(leaf)

                # If the neighbor itself becomes a leaf, push it to the queue
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        # The remaining nodes in the queue are the optimal roots (centroids)
        return list(leaves)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
    # Output: [3, 4]


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes. We look at every node and every edge
# exactly once during graph construction and processing, meaning it scales linearly.
# Space Complexity: O(N) auxiliary space required to map node connections inside the graph adjacency structure and
# to handle the FIFO leaves layer queue tracker.
