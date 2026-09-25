# Task description:
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.
#
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are
# non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104


# Greedy Algorithm via Interval Scheduling (Sorting by End Time)
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])

        # Track the end time of the last non-overlapping interval we decided to keep
        prev_end = intervals[0][1]
        erase_count = 0

        # Step 2: Iterate through the remaining intervals
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            # If the current interval starts before the previous one ends, it overlaps!
            if current_start < prev_end:
                erase_count += 1
            else:
                # No overlap, so we keep this interval and update the end boundary tracker
                prev_end = current_end

        return erase_count


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    # Output: 1
    print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    # Output: 2


# Time Complexity: O(NlogN), where N is the total number of elements inside the intervals array. Sorting the array 
# takes O(NlogN) time, while the subsequent greedy pass scans the list linearly in O(N) time. Thus, the initial 
# sorting step dominates the execution timeline.
# Space Complexity: O(N) worst-case or O(logN) auxiliary space depending on the internal implementation mechanics 
# of the sorting engine. Python’s native Timsort allocates dynamic memory slots to hold elements during structural 
# pivot runs. No extra data structures are instantiated by the algorithm logic itself.
