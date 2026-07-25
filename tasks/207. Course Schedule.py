# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course
# bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Examples
# Example 1
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So it is possible.

# Example 2
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1.
# So it is impossible.

# Constraints
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


# The solution using Kahn's Algorithm (Breadth-First Search / Topological Sort):


from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # 1. Build the adjacency list and in-degree array
    adj_list = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    # 2. Queue all nodes with 0 in-degree (no prerequisites)
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    # 3. Process the queue
    visited_courses = 0
    while queue:
        current = queue.popleft()
        visited_courses += 1

        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 4. If visited count matches total courses, no cycle exists
    return visited_courses == numCourses


if __name__ == "__main__":
    print(canFinish(2, [[1, 0]]))
    # True
    # print(canFinish(2, [[1, 0], [0, 1]]))
    # # False
    # print(canFinish(4, [[1, 0], [2, 1]]))
    # # True
