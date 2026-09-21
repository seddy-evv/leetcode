# Task description:
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations
# that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:
# Input: nums = [9], target = 3
# Output: 0

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation
# we need to add to the question to allow negative numbers?


# Dynamic Programming (Bottom-Up Tabulation)
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] will store the total number of combinations that sum up to i
        dp = [0] * (target + 1)

        # Base case: There is exactly 1 way to reach a sum of 0 (by picking nothing)
        dp[0] = 1

        # Compute combinations for every value from 1 up to target
        for i in range(1, target + 1):
            for num in nums:
                # If the current number can contribute to the sum i
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum4([1, 2, 3], 4))
    # Output: 7
    print(sol.combinationSum4([9], 3))
    # Output: 0


# Time Complexity: O(T*N), where T is the target value and N is the number of elements in the nums array. We run a
# nested combination loop computing state entries sequentially up to the target scale.
# Space Complexity: O(T) auxiliary space required to maintain the 1D state tracking list dp of size target + 1.
