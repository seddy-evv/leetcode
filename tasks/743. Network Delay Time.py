# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as
# directed edges times[i] = [ui, vi, wi], where ui is the source node, vi is the target node, and wi is the time
# it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
# (Note: The underlying algorithmic sub-problem here is calculating the single-source shortest path from city k
# to all other cities).
# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Explanation: The signal sent from node 2 reaches node 1 at time 1, node 3 at time 1, and node 4 at time 2. The maximum
# time taken is 2.
# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1


# Dijkstra's Algorithm (Using a Priority Queue / Min-Heap)
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize Dijkstra's tracking structures
        # Min-heap stores pairs of: (distance_from_source, current_node)
        min_heap = [(0, k)]

        # Dictionary to store the shortest distance to each visited node
        shortest_paths = {}

        # Step 3: Run Dijkstra's algorithm loop
        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            # If we've already found a shorter path to this node, skip it
            if current_node in shortest_paths:
                continue

            # Record the shortest path to this node
            shortest_paths[current_node] = current_dist

            # Explore all outgoing roads/edges to neighboring cities
            for neighbor, weight in graph[current_node]:
                if neighbor not in shortest_paths:
                    heapq.heappush(min_heap, (current_dist + weight, neighbor))

        # Step 4: Check if all cities/nodes were reached
        if len(shortest_paths) == n:
            # The total time is the maximum of the shortest paths to all nodes
            return max(shortest_paths.values())

        return -1


if __name__ == "__main__":

    sol = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(sol.networkDelayTime(times, n, k))
    # 2


# Complexity Analysis:
# Time Complexity: O(ElogV), where E is the number of edges (times.length) and V is the number of vertices (n).
# Each edge is pushed and popped from the min-heap at most once, and heap operations take logarithmic time.
# Space Complexity: O(V + E) to store the adjacency list graph structure and the shortest paths dictionary
