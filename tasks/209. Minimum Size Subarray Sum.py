# Task description:
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
# sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity
# is O(n log(n)).


# Sliding Window (specifically, a Variable-Size Sliding Window / Two-Pointer approach)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Initialize min_length to infinity so any valid window will be smaller
        min_length = float('inf')
        current_sum = 0
        left = 0

        # Expand the window using the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window from the left as long as the condition is met
            while current_sum >= target:
                # Update the minimal length found so far
                min_length = min(min_length, right - left + 1)

                # Remove the leftmost element and slide the left pointer forward
                current_sum -= nums[left]
                left += 1

        # If min_length was never updated, it means no valid subarray exists
        return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    # --- Example Usage ---
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))
    # 2
    # Explanation: The subarray [4,3] has the minimal length under the problem constraint.


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the nums array. Although there is a nested while loop, the left
# pointer can only move forward and will visit each element at most once during the entire execution.
# Space Complexity: O(1) auxiliary space, as we only use a few integer variables (left, current_sum, min_length)
# to track indices and data boundaries.
