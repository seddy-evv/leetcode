# Task description:
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
# to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


# Binary Search (Two-Pointer Divide and Conquer).
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Prevents potential integer overflow compared to (low + high) // 2
            mid = low + (high - low) // 2

            # Target found, return its index immediately
            if nums[mid] == target:
                return mid
            # If target is larger, discard the left half
            elif nums[mid] < target:
                low = mid + 1
            # If target is smaller, discard the right half
            else:
                high = mid - 1

        # Target was not found in the array
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test case matching Example 1
    sorted_array = [-1, 0, 3, 5, 9, 12]
    target_value = 9

    result = sol.search(sorted_array, target_value)
    print(f"Array: {sorted_array}, Target: {target_value}")
    print(f"Target found at index: {result}")
    # Output: 4


# Time Complexity: O(log N), where N is the total number of elements in the nums array. In each iteration of the loop,
# the algorithm cuts the active search area exactly in half, leading to a logarithmic runtime constraint.
# Space Complexity: O(1) constant auxiliary space. The lookups run entirely in-place using only three scalar pointer
# variables (low, high, and mid) tracking indexes natively in active memory.
