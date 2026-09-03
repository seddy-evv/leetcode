# Task description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Sorting and Two-Pointer Technique
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to safely use the two-pointer approach
        nums.sort()

        for i in range(len(nums)):
            # Skip duplicate values for the first element to avoid identical triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the current number is greater than 0, a sum of 0 is impossible
            # because the array is sorted and all subsequent numbers are positive
            if nums[i] > 0:
                break

            # Step 2: Use two pointers to find the remaining pair
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res


if __name__ == "__main__":
    # --- Example Usage ---
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # Output: [[-1, -1, 2], [-1, 0, 1]]


# Complexity Analysis:
# Time Complexity: O(N^2), where N is the length of the nums array. Sorting takes O(NlogN) time. The nested loops
# take O(N^2) because for each element, the two-pointer scan traverses the remainder of the array in linear time.
# The quadratic step dominates the runtime.
# Space Complexity: From O(1) to O(N) auxiliary space, depending entirely on the internal implementation of the
# sorting algorithm (nums.sort() uses Timsort in Python, which takes up to linear memory space). No extra collections
# are initialized to store combinations.
