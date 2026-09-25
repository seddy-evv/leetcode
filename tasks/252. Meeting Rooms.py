# Task description:
# Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend
# all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]] → Output: false
# Explanation: A person cannot attend all meetings because [0,30] overlaps with both [5,10] and [15,20].
# Example 2:
# Input: intervals = [[7,10],[2,4]] → Output: true


# Sorting-Based Conflict Detection.
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if not intervals:
            return True

        # Step 1: Sort the meetings by their start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Check for any overlapping intervals
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends, there is a conflict
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    # Output: False
    print(sol.canAttendMeetings([[7, 10], [2, 4]]))
    # Output: True


# Time Complexity: O(NlogN), where N is the total number of meetings. Sorting the list by start times takes
# O(NlogN) time, while the verification pass takes linear O(N) time. The sorting process dominates the runtime.
# Space Complexity: O(1) or O(N) depending on the programming language's internal sorting strategy. Python's Timsort
# uses up to linear memory space in the worst case to process tracking structures. No extra arrays are created by the
# algorithm itself.
