# Task description:
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that
# there is an undirected edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2
# Explanation: The nodes are split into two separate connected networks: {0, 1, 2} and {3, 4}.

# Example 2:Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# Output: 1
# Explanation: All nodes are linked together into a single component.


# Union-Find (Disjoint Set Union - DSU) with Path Compression and Rank Optimization
class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.components_count = size  # Tracks the active component count

    def find(self, i: int) -> int:
        """Finds the root representative of node i with Path Compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Unites components containing i and j using Union by Rank."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Rank optimization
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

            # Decrement the count since two distinct groups merged into one
            self.components_count -= 1


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)

        # Process each connection
        for u, v in edges:
            uf.union(u, v)

        return uf.components_count


# --- Corrected Example Usage ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Nodes 0-1-2 are connected, and 3-4 are connected. Total 2 components.
    edges1 = [[0, 1], [1, 2], [3, 4]]
    print(sol.countComponents(5, edges1))  # Output: 2

    # Test Case 2: All nodes connected together in a single chain. Total 1 component.
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(sol.countComponents(5, edges2))  # Output: 1


# Time Complexity: O(N + E*alpha(N)), where N is the number of nodes and E is the number of edges. The term α stands
# for the Inverse Ackermann function, which grows so slowly that it stays under 4 for all realistic inputs,
# effectively making each operation take O(1) constant time on average.
# Space Complexity: O(N) auxiliary space required to maintain the structural state tracking datasets (parent and rank)
# inside the UnionFind instance workspace.
