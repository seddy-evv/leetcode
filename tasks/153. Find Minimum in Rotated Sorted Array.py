# Task description:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
# nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


# Binary Search (Inflection Point Identification).
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        # Binary search loop
        while low < high:
            mid = low + (high - low) // 2

            # If the middle element is greater than the highest element,
            # the minimum element must be in the right unsorted half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # If the middle element is less than or equal to the highest element,
            # the minimum element is either at 'mid' or to its left side.
            else:
                high = mid

        # When low == high, it points directly to the minimum element
        return nums[low]


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
    # Output: 1
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    # Output: 0

# Time Complexity: O(log N), where N is the length of the nums array. The search space is divided in
# half during each iteration of the binary loop.
# Space Complexity: O(1) auxiliary space. Only three primitive integer pointer variables (low, high, mid)
# are tracked in memory.
