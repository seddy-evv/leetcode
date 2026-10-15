# Task description:
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of
# the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100


# Dynamic Programming (Space-Optimized 0/1 Knapsack Solution).
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, it's mathematically impossible to split it into two equal integer subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # dp[i] will be True if a subset sum of i can be formed
        dp = [False] * (target + 1)
        # Base case: A sum of 0 is always achievable (by choosing an empty subset)
        dp[0] = True

        for num in nums:
            # Loop backward from target down to num to avoid using the current 'num' more than once
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

            # Early exit optimization: if the target sum is already achievable, we can return True immediately
            if dp[target]:
                return True

        return dp[target]


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 matching Example 1
    nums1 = [1, 5, 11, 5]
    print(f"Array: {nums1} -> Can partition? {sol.canPartition(nums1)}")
    # Array: [1, 5, 11, 5] -> Can partition? True

    # Test Case 2 matching Example 2
    nums2 = [1, 2, 3, 5]
    print(f"Array: {nums2} -> Can partition? {sol.canPartition(nums2)}")
    # Array: [1, 2, 3, 5] -> Can partition? False


# Time Complexity: O(N*T), where N is the length of the nums array and T is the target sum (total_sum // 2). We use
# a nested loop where the outer layer runs N times and the inner layer runs up to T times.
# Space Complexity: O(T) auxiliary space. By optimizing the knapsack matrix down to a single 1D state array,
# the memory allocation is proportional only to the size of the target sum value.
