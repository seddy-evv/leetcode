# Task description:
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


# Prefix Sum with Hash Map (Dictionary) Lookups.
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0

        # Hash map to store: prefix_sum -> frequency of occurrence
        # Base case: A prefix sum of 0 has occurred exactly 1 time (empty prefix)
        prefix_sums = {0: 1}

        for num in nums:
            # Update the running cumulative sum
            current_sum += num

            # If (current_sum - k) exists in our map, it means a valid
            # subarray ending at the current index sums up to k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Record the current running sum into the hash map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, -1, 1, 1, 1], 2))
    # Output: 4


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the nums array. We perform a single pass through the
# array, and looking up or updating keys in the hash map takes O(1) time on average.
# Space Complexity: O(N) auxiliary space to store the prefix sum frequencies inside the prefix_sums dictionary in
# the worst-case scenario where every single prefix sum is unique.
