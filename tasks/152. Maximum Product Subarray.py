# Task description:
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


# Dynamic Programming (Kadane's Algorithm Variant for Products).
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Initialize global max, along with local max and min running products
        global_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            # If the current number is negative, multiplying it swaps the max and min values.
            # E.g., a huge positive max becomes a huge negative min, and vice versa.
            if num < 0:
                current_max, current_min = current_min, current_max

            # The new max/min at the current index can either be the number itself
            # (starting a new subarray) or the number multiplied by the previous max/min.
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            # Update the absolute largest product found so far
            global_max = max(global_max, current_max)

        return global_max


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))  # Output: 6
    print(sol.maxProduct([-2, 3, -4]))  # Output: 24 (From subarray [-2, 3, -4])

# Time Complexity: O(N), where N is the length of the nums array. We perform a single linear sweep across the list, 
# updating the state variables in constant time at each index.
# Space Complexity: O(1) auxiliary space. Only three local scalar variables (global_max, current_max, and current_min) 
# are maintained natively in memory, using no structural tracking structures.
