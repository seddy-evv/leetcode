# Task description:
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all
# the elements in the subarray is strictly less than k.

# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0


# Constraints:
#
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


# Sliding Window (specifically, a Two-Pointer approach)
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Edge case: if k is 0 or 1, no product of positive integers can be strictly less than k
        if k <= 1:
            return 0

        total_count = 0
        current_product = 1
        left = 0

        # Expand the window using the right pointer
        for right in range(len(nums)):
            current_product *= nums[right]

            # Shrink the window from the left if the product is not less than k
            while current_product >= k and left <= right:
                current_product //= nums[left]
                left += 1

            # The number of valid subarrays ending at the 'right' index
            # is equal to the current window size (right - left + 1)
            total_count += (right - left + 1)

        return total_count


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    sol = Solution()
    res = sol.numSubarrayProductLessThanK(nums, k)
    print(res)
    # 8

# Complexity Analysis:
# Time Complexity: O(N) where N is the length of the nums array. Although there is a nested while loop, the left
# pointer can only move forward at most N times across the entire execution.
# Space Complexity: O(1) extra space, as we only use a few pointer and product variables.
