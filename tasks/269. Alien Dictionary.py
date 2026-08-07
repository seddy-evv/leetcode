# There is a new alien language that uses the Latin alphabet. However, the order of the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary, where the strings are sorted
# lexicographically according to the rules of this new language.
# Return a string of the unique letters in the new alien language sorted in a valid lexicographically increasing order
# by the new language's rules. If there is no valid ordering of letters, return "". If there are multiple valid
# solutions, return any of them.
# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Example 2:
# Input: words = ["z","x"]
# Output: "zx"

# Example 3:
# Input: words = ["z","x","z"]
# Output: "" (Explanation: The order is invalid because 'z' cannot come before 'x' and 'x' cannot come before 'z'
# simultaneously).


# Topological Sort (Kahn's Algorithm / BFS approach)
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # Step 1: Initialize the graph adj list and in-degree map for all unique characters
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build the graph edges by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[j := i + 1]
            min_len = min(len(w1), len(w2))

            # Edge Case: An invalid sorting prefix scenario like ["abc", "ab"]
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    parent, child = w1[j], w2[j]
                    if child not in graph[parent]:
                        graph[parent].add(child)
                        in_degree[child] += 1
                    break  # Only the first differing character establishes the order

        # Step 3: Add all characters with an in-degree of 0 to the queue
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        # Step 4: Run Topological Sort (Kahn's BFS Process)
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check if the graph contains a cycle
        if len(result) < len(in_degree):
            return ""

        return "".join(result)


if __name__ == "__main__":

    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(sol.alienOrder(words))
    # wertf


# Complexity Analysis:
# Time Complexity: O(C), where C is the total length of all characters across all words combined.
# Building the graph and processing the nodes/edges via Topological sort iterates through the content linearly.
# Space Complexity: O(V + E). Since the alphabet is capped at 26 lowercase English characters, the total vertices
# V ≤ 26 and edges E ≤ 26², matching strict O(1) constant auxiliary space bounds.
