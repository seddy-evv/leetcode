# Task description:
# You are given an integer array coins representing coins of different denominations and an integer amount representing
# a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
# any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


# Dynamic Programming (specifically, the Bottom-Up approach using a 1D array)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize the DP table with a value greater than any possible solution
        # amount + 1 is safe because the maximum coins needed cannot exceed amount (if using 1-value coins)
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0

        # Compute the minimum coins for every amount from 1 to 'amount'
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] was not updated, it means the amount cannot be formed
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    res = sol.coinChange(coins, amount)
    print(res)
    # 3

# Complexity Analysis:
# Time Complexity: O(NxA), where N is the number of coin denominations and A is the target amount. We run a
# nested loop through all amounts up to A for every single coin.
# Space Complexity: O(A) to store the dp array of size amount + 1.
