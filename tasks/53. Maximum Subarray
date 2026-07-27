# Task Description
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Examples
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints
# 1 <= nums.length ≤ 10**5
# -10**4 <= nums[i] <= 10**4


# It is optimally solved using Kadane's Algorithm in a single pass:

def maxSubArray(nums: list[int]) -> int:
    # Initialize both tracking variables with the first element
    max_global = nums[0]
    max_current = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Decide whether to add the current element to the existing subarray
        # or start a brand new subarray from the current element
        max_current = max(nums[i], max_current + nums[i])

        # Update the global maximum if the current subarray sum is higher
        if max_current > max_global:
            max_global = max_current

    return max_global


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # 6


# Complexity Analysis
# Time Complexity: O(N) since we iterate through the array of length N exactly once.
# Space Complexity: O(1) because we only use two scalar variables (max_current and max_global) to track sums
# without allocating extra data structures.
