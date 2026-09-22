# Task description:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
# two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


# Dynamic Programming (Linear Reduction of Circular State Space).
class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge case: If there is only one house, rob it directly
        if len(nums) == 1:
            return nums[0]

        def rob_linear(house_range: list[int]) -> int:
            """Standard space-optimized linear House Robber I helper."""
            rob_prev2 = 0
            rob_prev1 = 0

            for current_money in house_range:
                temp = max(rob_prev1, rob_prev2 + current_money)
                rob_prev2 = rob_prev1
                rob_prev1 = temp

            return rob_prev1

        # Return the maximum between excluding the last house or excluding the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))  # Output: 3
    print(sol.rob([1, 2, 3, 1]))  # Output: 4


# Time Complexity: O(N), where N is the total number of houses. We perform two consecutive linear passes over arrays
# of length N-1, yielding 2*O(N) = O(N).
# Space Complexity: O(1) auxiliary space if we use array slicing or index boundaries carefully. The local tracking
# registers (rob_prev1 and rob_prev2) roll over dynamically in scalar memory, requiring no structural matrix allocation.
