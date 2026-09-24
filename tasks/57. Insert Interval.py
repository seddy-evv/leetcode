# Task description:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
# the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given
# an interval newInterval = [start, end] that represents the start and end of another interval.

# Two intervals are considered overlapping if they share at least one point.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105


# Linear Scan with Greedy Interval Merging
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that end before the newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            # The new start is the minimum of both starts
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # The new end is the maximum of both ends
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Append the completely merged newInterval
        result.append(newInterval)

        # Step 3: Add all remaining intervals that start after the newInterval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))
    # Output: [[1, 5], [6, 9]]

    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    # Output: [[1, 2], [3, 10], [12, 16]]


# Time Complexity: O(N), where N is the total number of intervals. We perform a single sequential loop through
# the intervals array using a pointer index i. This avoids sorting the list again, which would take O(NlogN) time.
# Space Complexity: O(1) auxiliary space if we exclude the memory allocated to store the final result list.
# The calculation runs inline using only a few constant control variables.
