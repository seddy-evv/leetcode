# Task description:
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


# Cycle Sort / Cyclic Placement (In-Place Array Partitioning).
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct bucket/index slot if possible
        for i in range(n):
            # Keep swapping until nums[i] is at its correct index (nums[i] - 1)
            # Conditions to swap:
            # 1. The number is positive: nums[i] > 0
            # 2. The number fits within the array bounds: nums[i] <= n
            # 3. The target slot doesn't already contain the correct number to avoid infinite loops
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Find the first index where the slot number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all positions 1 to n are correct, the missing number is n + 1
        return n + 1


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    # Output: 2


# Time Complexity: O(N), where N is the length of the nums array. Although there is a nested while loop, each swap
# operation places at least one element into its final correct position. Since an element can be correctly placed at
# most once, the inner loop body executes a total maximum of N times across the entire program.
# Space Complexity: O(1) auxiliary space. We rearrange the integers entirely in-place within the input array without
# allocating extra sets or tracking collections.
