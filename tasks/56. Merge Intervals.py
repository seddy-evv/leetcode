# Task description:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Example 3:
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Sorting and Greedy Interval Merging.
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Edge case: if there are no intervals or only one, no merging is needed
        if not intervals:
            return []

        # Step 1: Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        # Initialize the list of merged intervals with the first interval
        merged = [intervals[0]]

        # Step 2: Iterate through the remaining intervals
        for current in intervals[1:]:
            # Get the last merged interval to compare boundaries
            last_merged = merged[-1]

            # If the current interval overlaps with the last merged interval
            # (i.e., current start time is less than or equal to the last end time)
            if current[0] <= last_merged[1]:
                # Merge them by updating the end time to the maximum of both
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, so safely add the current interval to the list
                merged.append(current)

        return merged


if __name__ == "__main__":
    # Create an instance of the solution
    sol = Solution()

    # Test case matching the problem description
    transaction_intervals = [[1, 3], [2, 6], [8, 10]]
    result = sol.merge(transaction_intervals)

    print(f"Merged intervals: {result}")
    # Merged intervals: [[1, 6], [8, 10]]

# Complexity Analysis:
# Time Complexity: O(NlogN), where N is the total number of intervals. Sorting the array takes O(NlogN) time. The
# subsequent linear scan to merge intervals takes O(N) time. Thus, the sorting step dominates the runtime.
# Space Complexity: O(N) or O(log N) depending on the implementation details. We require O(N) memory to store the
# output array. If we ignore output space, Python's built-in Timsort requires O(N) worst-case auxiliary space to
# handle the sorting process.


# Key Interview Talking Points
# - The Power of Sorting: Explain to the interviewer that sorting the intervals by their start time transforms a
# complex combinations problem into a straightforward linear scan. Once sorted, an interval can only possibly overlap
# with the interval immediately preceding it in our merged tracker.
# - The max() Comparison Trap: Point out why max(last_merged[1], current[1]) is necessary. A common bug is assuming
# current[1] is always larger. However, an interval can completely engulf another one (e.g., merging [[1, 10], [2, 5]]
# should yield [[1, 10]]).
# - Real-World Application: In financial systems, this pattern is extensively used to group overlapping trading
# sessions, aggregate lockup periods, or consolidate timestamps of high-frequency transactions to map out system
# activity windows.
