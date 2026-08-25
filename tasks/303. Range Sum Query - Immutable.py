# Task description:
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
# (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example 1:
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# Prefix Sum technique.
class NumArray:

    def __init__(self, nums: list[int]):
        # Create a prefix sum array padded with an initial 0.
        # prefix_sums[i] will store the sum of nums from index 0 to i-1.
        self.prefix_sums = [0] * (len(nums) + 1)

        # Build the prefix sum array
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # The sum of elements from index 'left' to 'right' inclusive
        # is equal to prefix_sums[right + 1] minus prefix_sums[left]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


if __name__ == "__main__":
    # --- Example Usage ---
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2)) # Returns 1  -> (-2 + 0 + 3)
    print(obj.sumRange(2, 5)) # Returns -1 -> (3 + -5 + 2 + -1)
    print(obj.sumRange(0, 5)) # Returns -3 -> (-2 + 0 + 3 + -5 + 2 + -1)


# Complexity Analysis:
# Time Complexity:Initialization (__init__): O(N) where N is the length of the array, as we iterate
# through the list once to build the prefix sums.Query (sumRange): O(1) constant time, because it only
# performs a single subtraction operation regardless of how large the requested range is.
# Space Complexity: O(N) auxiliary space to store the precomputed prefix sum array of size N + 1.
