# You are given an array prices where prices[i] is the price of a given stock on the i^th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5. Note that buying on
# day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0Explanation: In this case, no transactions are done and the max profit = 0.


# Sliding Window (Two Pointers / Two-Pointer Approach)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 'left' is the buy day, 'right' is the sell day
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            # If the current window shows a profitable transaction
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # We found a lower price than our original buy price.
                # Slide the left window pointer directly to this new lower point.
                left = right

        return max_profit


if __name__ == "__main__":

    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
    # 5


# Complexity Analysis:
# Time Complexity: O(n), where n is the number of days in the prices array. The right pointer scans through the array
# exactly once, making the time complexity linear.
# Space Complexity: O(1) auxiliary space. The algorithm runs entirely in-place, relying only on two integer pointers
# to track the window boundaries.
