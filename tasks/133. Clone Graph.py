# Task description:
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
# val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set
# of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference
# to the cloned graph.

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it
# does not have any neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.


# Breadth-First Search (BFS) with Hash Map Tracking
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to save visited nodes and map the original node to its clone.
        # This prevents infinite loops in cyclical graphs.
        visited = {}

        # Clone the root node and place it in the visited dictionary
        visited[node] = Node(node.val)

        # Queue for standard BFS traversal
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()

            # Iterate through all neighbors of the current node
            for neighbor in curr_node.neighbors:
                # If the neighbor hasn't been cloned yet
                if neighbor not in visited:
                    # Deep copy the neighbor node
                    visited[neighbor] = Node(neighbor.val)
                    # Append the original neighbor to the queue to traverse its connections later
                    queue.append(neighbor)

                # Link the clone of the current node to the clone of the neighbor node
                visited[curr_node].neighbors.append(visited[neighbor])

        # Return the clone of the initial starting node
        return visited[node]


# --- Verification & Simulation Setup ---
if __name__ == "__main__":
    # Create an original cyclical graph matching LeetCode Example 1:
    # 1 <---> 2
    # ^       ^
    # |       |
    # v       v
    # 4 <---> 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # Run the Deep Cloning algorithm
    sol = Solution()
    cloned_node1 = sol.cloneGraph(node1)

    # --- Deep Copy Verification Tests ---
    print(f"Original Node 1 Memory Address: {id(node1)}")
    # Original Node 1 Memory Address: 1514440982480
    print(f"Cloned Node 1 Memory Address:   {id(cloned_node1)}")
    # Cloned Node 1 Memory Address:   1514440967600
    print(f"Are they completely different objects? {id(node1) != id(cloned_node1)}")
    # Are they completely different objects? True

    print("\n--- Structural Neighbors Audit ---")
    print(f"Original Node 1 value: {node1.val}, neighbor values: {[n.val for n in node1.neighbors]}")
    # Original Node 1 value: 1, neighbor values: [2, 4]
    print(f"Cloned Node 1 value:   {cloned_node1.val}, neighbor values: {[n.val for n in cloned_node1.neighbors]}")
    # Cloned Node 1 value:   1, neighbor values: [2, 4]

    # Check that neighbors are also cloned objects, not pointers back to old memory
    cloned_neighbor_address = id(cloned_node1.neighbors[0])
    original_neighbor_address = id(node1.neighbors[0])
    print(f"Are neighbor objects deep copies too? {cloned_neighbor_address != original_neighbor_address}")
    # Are neighbor objects deep copies too? True


# Time Complexity: O(N + E), where N is the number of nodes (vertices) and E is the number of edges in the graph.
# The BFS algorithm visits every unique node exactly once and processes every edge to copy the adjacent links.
# Space Complexity: O(N) auxiliary space. The visited hash map holds a mapping for all N cloned nodes, and the queue
# can hold up to N nodes at its widest traversal boundary.
