# Task description:
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
# edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# A graph is a valid tree if and only if it satisfies two conditions:
# 1. It is fully connected (there is a path between any two nodes).
# It contains no cycles.
# Example 1: Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]] → Output: true
# Example 2: Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]] → Output: false (Contains a cycle 1-2-3-1).


# Union-Find (Disjoint Set Union - DSU) with Path Compression and Rank Optimization.
class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, i: int) -> int:
        """Finds the root of node i with Path Compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """
        Unites components containing i and j using Union by Rank.
        Returns False if i and j are already connected (indicating a cycle).
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False  # Nodes are already connected; a cycle is detected!

        # Union by Rank optimization
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Condition 1: A valid tree with 'n' nodes MUST have exactly 'n - 1' edges.
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        # Condition 2: Check for cycles while processing edges
        for u, v in edges:
            if not uf.union(u, v):
                return False  # Cycle detected

        return True


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    # Output: True
    print(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    # Output: False


# Time Complexity: O(N*alpha(N)), where N is the number of nodes. The function alpha represents the Inverse Ackermann
# function, which grows so incredibly slowly that it is effectively a constant O(1) for all practical purposes.
# This makes the execution speed nearly linear O(N).
# Space Complexity: O(N) auxiliary space required to store the tracking arrays (parent and rank) within the Union-Find
# structure.
