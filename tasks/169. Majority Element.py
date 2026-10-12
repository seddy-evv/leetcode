# Task description:
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.

# Follow-up: Could you solve the problem in linear time and in O(1) space?


# Boyer-Moore Voting Algorithm.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Initialize the candidate element and its net voting count
        candidate = None
        count = 0

        for num in nums:
            # If count drops to 0, dynamically pick the current number as the new candidate
            if count == 0:
                candidate = num

            # Increment the count if the number matches our candidate; decrement otherwise
            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 matching Example 1
    nums1 = [3, 2, 3]
    print(f"Majority element for {nums1}: {sol.majorityElement(nums1)}")  # Output: 3

    # Test Case 2 matching Example 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Majority element for {nums2}: {sol.majorityElement(nums2)}")  # Output: 2


# Time Complexity: O(N), where N is the length of the nums array. The algorithm sweeps through the array exactly once 
# in a single linear pass.
# Space Complexity: O(1) auxiliary space. Only two primitive variables (candidate and count) are tracked in 
# active memory, satisfying the optimal follow-up constraint of using constant extra memory space.
