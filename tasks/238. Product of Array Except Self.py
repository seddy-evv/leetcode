# Task description:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
# for space complexity analysis.)


# Prefix and Suffix Products (Space-Optimized Dual Pass).
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Initialize the output array where answer[i] will store the cumulative products
        answer = [1] * n

        # Step 1: Compute the prefix product for each element
        # answer[i] will contain the product of all elements to the left of index i
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Step 2: Compute the suffix product and multiply it with the prefix product
        # suffix_product will track the running product of all elements to the right of index i
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    # Output: [24, 12, 8, 6]

# Time Complexity: O(N), where N is the length of the nums array. We perform exactly two distinct linear passes over 
# the array (one forward pass and one backward pass).
# Space Complexity: O(1) auxiliary space. The problem specification states that the output array does not count as 
# extra space for the purpose of space complexity analysis. Aside from the answer list, we only use a few constant 
# variables (prefix_product, suffix_product, i).
