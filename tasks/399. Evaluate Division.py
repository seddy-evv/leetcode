# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
# and values[i] represent the equation A_i / B_i = values[i]. Each A_i or B_i is a string that represents a single
# variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the j-th query where you must find the value
# of C_j / D_j.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.


# Graph Map Modeling with Depth-First Search (DFS)
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # Step 1: Construct the map graph adjacency list
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        # Helper function: Recursive DFS map traversal
        def dfs(curr, target, visited):
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0

            visited.add(curr)

            # Explore neighboring roads on the map
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight * product

            return -1.0

        # Step 2: Evaluate each query on our graph map
        results = []
        for src, dest in queries:
            results.append(dfs(src, dest, set()))

        return results


if __name__ == "__main__":

    sol = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(sol.calcEquation(equations, values, queries))
    # [6.0, 0.5, -1.0, 1.0, -1.0]


# Complexity Analysis:
# Time Complexity: O(M * (V + E)), where M is the number of queries, V is the number of variables, and E is the
# number of equations. For each query, we perform a standard map traversal.
# Space Complexity: O(V + E) to maintain the graph database in memory.
