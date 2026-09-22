# Task description:
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in
# the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
# impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


# Greedy Algorithm (Furthest Reach Tracking).
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Tracks the maximum index we can currently reach
        max_reachable = 0
        target = len(nums) - 1

        for i, jump in enumerate(nums):
            # If the current index is greater than the furthest reachable point,
            # it means we hit a dead end and cannot proceed further.
            if i > max_reachable:
                return False

            # Update the furthest index we can reach from the current spot
            max_reachable = max(max_reachable, i + jump)

            # Optimization: If the furthest reachable point meets or exceeds
            # the last index, we can successfully finish early.
            if max_reachable >= target:
                return True

        return max_reachable >= target


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))  
    # Output: True
    print(sol.canJump([3, 2, 1, 0, 4]))  
    # Output: False


# Time Complexity: O(N), where N is the length of the nums array. We perform a single linear pass over the array,
# updating the reachable boundary in constant time.
# Space Complexity: O(1) auxiliary space. Only a couple of scalar integer variables (max_reachable, target) are
# maintained in memory, requiring no structural matrix or tracking array allocation.
