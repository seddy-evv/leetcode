# Task description:
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

# Example 1:
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Constraints:
#
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107


# Frequency Counting Hash Mapping (Hash Set Lookups).
from collections import Counter


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        # Edge case: An absolute difference cannot be negative in this context
        if k < 0:
            return 0

        # Build a frequency map of all elements
        counts = Counter(nums)
        pair_count = 0

        for num in counts:
            if k == 0:
                # Edge case: If k == 0, a pair can only be formed
                # if the number appears at least twice (e.g., [1, 1])
                if counts[num] > 1:
                    pair_count += 1
            else:
                # Standard case: Check if the required complement (num + k) exists
                if num + k in counts:
                    pair_count += 1

        return pair_count


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPairs([3, 1, 4, 1, 5], 2))  # Output: 2
    print(sol.findPairs([1, 3, 1, 5, 4], 0))  # Output: 1


# Time Complexity: O(N), where N is the length of the nums array. Populating the frequency count map
# takes O(N) time, and iterating through the distinct keys takes O(U) steps where U ≤ N.
# Dictionary value checks run in constant O(1) time on average.
# Space Complexity: O(N) auxiliary space required to maintain the unique keys and their matching element frequency
# scores inside the Counter data map.
