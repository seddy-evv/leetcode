# Task description:
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return
# the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

# Constraints:
# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104


# Max-Heap Boundary Filtering
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Max-heap to store the k closest points seen so far
        max_heap = []

        for x, y in points:
            # Calculate the squared Euclidean distance
            dist = x ** 2 + y ** 2

            # Python's heapq is a min-heap by default.
            # We invert the distance sign (-dist) to simulate a max-heap structure.
            heapq.heappush(max_heap, (-dist, [x, y]))

            # If the heap size exceeds k, evict the point with the largest distance
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the point coordinates from the remaining items in the heap
        return [point for dist, point in max_heap]


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 2
    points_input = [[3, 3], [5, -1], [-2, 4]]
    k_value = 2

    result = sol.kClosest(points_input, k_value)
    print(f"Points bank: {points_input}, k = {k_value}")
    # Points bank: [[3, 3], [5, -1], [-2, 4]], k = 2
    print(f"The {k_value} closest points are: {result}")
    # The 2 closest points are: [[-2, 4], [3, 3]]


# Time Complexity: O(NlogK), where N is the total number of items in the points array and K is the target quantity.
# We iterate through all N elements sequentially. Maintaining the heap boundary at size K limits insertion and
# extraction operations to O(log K) steps, outperforming a complete sort algorithm O(Nlog N).
# Space Complexity: O(K) auxiliary space required to maintain the coordinates of the closest candidate markers inside
# the tracking max_heap layer.
