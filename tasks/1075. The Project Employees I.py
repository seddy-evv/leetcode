# Given a list of scores of different students, items, where items[i] = [IDi, scorei] represents that the student
# with IDi got scorei in an exam.
# Find the average of the top five highest scores for each student. Return the answer as a list of pairs
# [IDi, topFiveAverage], where topFiveAverage is rounded down using integer division. The output should be sorted by
# IDi in ascending order.
# Example 1:
# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
#   Student 1's scores are [91, 92, 60, 65, 87, 100]. Their top 5 scores are [100, 92, 91, 87, 65]. The average is
#   (100 + 92 + 91 + 87 + 65) // 5 = 435 // 5 = 87.
#   Student 2's scores are [93, 97, 77, 100, 76]. Since they only have 5 scores, we take all of them. The average
#   is (100 + 97 + 93 + 77 + 76) // 5 = 443 // 5 = 88.


# Min-Heap with Grouped HashMap Mapping
import heapq
from collections import defaultdict


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        # Map student ID to a min-heap tracking their top 5 scores
        student_scores = defaultdict(list)

        for student_id, score in items:
            heapq.heappush(student_scores[student_id], score)

            # If we exceed 5 scores, evict the smallest score
            if len(student_scores[student_id]) > 5:
                heapq.heappop(student_scores[student_id])

        result = []

        # Sort by student ID to fulfill the ascending requirement
        for student_id in sorted(student_scores.keys()):
            # The heap contains exactly the top 5 scores
            top_5_sum = sum(student_scores[student_id])
            average = top_5_sum // 5  # Integer division rounding down
            result.append([student_id, average])

        return result


if __name__ == "__main__":

    sol = Solution()
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    print(sol.highFive(items))
    # [[1, 87], [2, 88]]


# Complexity Analysis:
# Time Complexity: O(Nlog K + MlogM), where N is the total number of items, K is the max size of the heap
# (which is capped at a constant 5, so log 5=O(1)), and M is the number of unique students sorted at the end.
# This is practically a linear time operation O(N)
# Space Complexity: O(M) auxiliary space to store up to 5 elements per unique student within our tracking map
