# Task Description
# Given an unsorted integer array nums, reorder it in-place such that it follows a alternating "wiggle" pattern:
# nums[0] <= nums[1] >= nums[2] <= nums[3]...

# Example:
# Input: nums = [3, 5, 2, 1, 6, 4]
# Output: [3, 5, 1, 6, 2, 4] (or any other valid arrangement)


# Greedy One-Pass Swap Algorithm
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            # Condition 1: At an odd index, the current number should be >= the previous number.
            # If it's smaller, we need to swap them.
            if i % 2 == 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

            # Condition 2: At an even index, the current number should be <= the previous number.
            # If it's larger, we need to swap them.
            elif i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return nums


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    sol = Solution()
    res = sol.wiggleSort(nums)
    print(res)
    # [3, 5, 1, 6, 2, 4]

# Complexity Analysis:
# Time Complexity: O(n) — The algorithm loops through the array exactly once, making a linear scan. n represents the
# total number of elements present in the input array nums
# Space Complexity: O(1) — The operations are done entirely in-place without using extra memory storage.
