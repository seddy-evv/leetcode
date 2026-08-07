# You are given an integer array score of size n, where score[i] is the score of the i-th student in a competition.
# All the scores are guaranteed to be unique.
# The elements are ranked from highest to lowest:
# The 1st place student gets the "Gold Medal".
# The 2nd place student gets the "Silver Medal".
# The 3rd place student gets the "Bronze Medal".
# For the 4th place to the n-th place student, their rank is simply their placement number as a string (e.g., "4").
# Return an array answer of size n where answer[i] is the rank awarded to the i-th student.


# Sorting with Index Mapping (Hash Map Association)
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Pair each score with its original index, then sort by score descending
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        result = [""] * len(score)

        for rank, (original_index, val) in enumerate(sorted_scores):
            if rank == 0:
                result[original_index] = "Gold Medal"
            elif rank == 1:
                result[original_index] = "Silver Medal"
            elif rank == 2:
                result[original_index] = "Bronze Medal"
            else:
                result[original_index] = str(rank + 1)

        return result


if __name__ == "__main__":

    sol = Solution()
    score = [10, 3, 8, 9, 4]
    print(sol.findRelativeRanks(score))
    # ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']


# Complexity Analysis:
# Time Complexity: O(nlogn)) due to sorting the scores.
# Space Complexity: O(n) to hold the tracking pairs and result lists.
