# Task description:
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


# Modified Binary Search (Segment-Based Evaluation).
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Target found immediately
            if nums[mid] == target:
                return mid

            # Case 1: The left half [low ... mid] is perfectly sorted
            if nums[low] <= nums[mid]:
                # Check if target falls strictly within the sorted left boundaries
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1  # Search right

            # Case 2: The right half [mid ... high] must be perfectly sorted
            else:
                # Check if target falls strictly within the sorted right boundaries
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Search right
                else:
                    high = mid - 1  # Search left

        return -1


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    # Output: 4
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
    # Output: -1

# Time Complexity: O(log N), where N is the length of the nums array. At each decision point, the algorithm divides
# the lookups in half, preserving traditional binary search speed despite the array rotation.
# Space Complexity: O(1) auxiliary space. Only three numerical scalar variables (low, high, mid) are tracked in active
# memory.
