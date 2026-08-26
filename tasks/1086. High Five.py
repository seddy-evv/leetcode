# Task description:
# You are given a 2D string array scores where each element is a pair [student_name, score]. A student can have
# multiple scores from different subjects.
# Find the maximum average score achieved by any student. If the average result is a decimal, calculate the floor
# value (nearest lower integer).

# Example:
# Input: scores = [["Bob", "87"], ["Mike", "35"], ["Bob", "52"], ["Jason", "35"], ["Mike", "99"]]
# Output: 69
# Explanation:
# Bob's average: (87 + 52) / 2 = 69.5 -> 69.
# Mike's average: (35 + 99) / 2 = 67.
# Jason's average: 35 / 1 = 35.
# The maximum of these averages is 69.


# Hash Map Aggregation with Fractional Tracking.
import math
from collections import defaultdict


class Solution:
    def highestAverageScore(self, scores: list[list[str]]) -> int:
        if not scores:
            return 0

        # Hash map to store: student_name -> [total_sum, count_of_subjects]
        student_data = defaultdict(lambda: [0, 0])

        # Step 1: Aggregate totals and counts for each student
        for name, score_str in scores:
            score = int(score_str)
            student_data[name][0] += score  # Add to total sum
            student_data[name][1] += 1  # Increment subject count

        max_avg = -float('inf')

        # Step 2: Compute floor average for each student and find the maximum
        for name, (total_sum, count) in student_data.items():
            # Use math.floor() to round down to the nearest integer
            current_avg = math.floor(total_sum / count)
            if current_avg > max_avg:
                max_avg = current_avg

        return max_avg


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    test_scores = [["Bob", "87"], ["Mike", "35"], ["Bob", "52"], ["Jason", "35"], ["Mike", "99"]]
    print(sol.highestAverageScore(test_scores))
    # Output: 69


# Complexity Analysis:
# Time Complexity: O(N), where N is the total number of entries in the scores array. We iterate
# through the initial array once to build our hash map statistics and then scan the unique keys of the map to compute
# averages.
# Space Complexity: O(U) auxiliary space, where U is the number of unique student names. The hash
# map stores one list record per unique student
