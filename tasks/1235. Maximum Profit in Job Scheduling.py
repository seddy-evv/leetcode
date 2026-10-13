# Task description:
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of
# profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there
# are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# Example 1:
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

# Example 2:
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.

# Example 3:
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6

# Constraints:
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 104
# 1 <= startTime[i] < endTime[i] <= 109
# 1 <= profit[i] <= 104


# Dynamic Programming with Binary Search (Interval Scheduling Optimization).
import bisect


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # Step 1: Zip the jobs together and sort them by their end times
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # Step 2: Initialize DP structures
        # dp_end_times will store sorted end times of valid job choices
        # dp_profits will store the maximum profit achievable up to those end times
        dp_end_times = [0]
        dp_profits = [0]

        for start, end, current_profit in jobs:
            # Step 3: Use binary search to find the latest non-overlapping job.
            # bisect_right finds the first end time greater than our current job's start time.
            idx = bisect.bisect_right(dp_end_times, start) - 1

            # Step 4: Calculate the total profit if we include this current job
            include_profit = dp_profits[idx] + current_profit

            # Step 5: If including this job breaks our previous peak profit record, save it
            if include_profit > dp_profits[-1]:
                dp_end_times.append(end)
                dp_profits.append(include_profit)

        return dp_profits[-1]


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 1
    start = [1, 2, 3, 3]
    end = [3, 4, 5, 6]
    prof = [50, 10, 40, 70]

    result = sol.jobScheduling(start, end, prof)
    print(f"Maximum Profit: {result}")
    # Output: 120


# Time Complexity: O(NlogN), where N is the total number of jobs. Sorting the intervals chronologically by their end
# times takes O(NlogN) time. The subsequent loop sweeps through the collection in O(N) steps, running a quick binary
# search using bisect_right on each iteration which costs O(log N). Thus, the sorting step sets the runtime limit.
# Space Complexity: O(N) auxiliary space required to merge and process the zipped intervals inside the sorted jobs
# list structure alongside the state monitoring arrays (dp_end_times and dp_profits).
