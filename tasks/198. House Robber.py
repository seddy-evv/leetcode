# Task description:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


# Dynamic Programming (Space-Optimized Bottom-Up Tabulation)
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Track the maximum money robbed up to two houses ago and one house ago
        rob_prev2 = 0
        rob_prev1 = 0

        for current_house_money in nums:
            # For the current house, choose the maximum between:
            # 1. Skipping this house: keeping the profit from the previous house (rob_prev1)
            # 2. Robbing this house: adding current money to the profit from two houses ago (rob_prev2)
            temp = max(rob_prev1, rob_prev2 + current_house_money)

            # Slide our state variables forward for the next iteration
            rob_prev2 = rob_prev1
            rob_prev1 = temp

        return rob_prev1


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 7, 9, 3, 1]))
    # 12

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of houses. We perform a single loop through the nums array exactly once.
# Space Complexity: O(1) auxiliary space. By using two scalar tracking variables (rob_prev1 and rob_prev2) to
# dynamically roll over values, we eliminate the need for a full Dynamic Programming array.

