# Task description:
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


# Monotonic Deque (Sliding Window Maximum Optimization).
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []

        result = []
        # Stores indices of elements, maintaining a decreasing order of values
        mon_deque = deque()

        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current sliding window bounds
            if mon_deque and mon_deque[0] < i - k + 1:
                mon_deque.popleft()

            # 2. Maintain monotonic property: remove indices of all elements
            # that are smaller than the current element 'num' from the back
            while mon_deque and nums[mon_deque[-1]] < num:
                mon_deque.pop()

            # 3. Append the current element's index
            mon_deque.append(i)

            # 4. Once the window reaches size k, append the maximum to our results
            if i >= k - 1:
                result.append(nums[mon_deque[0]])

        return result


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # Output: [3, 3, 5, 5, 6, 7]


# Time Complexity: O(N), where N is the length of the nums array. Although there is a nested while loop, every element 
# index is pushed into and popped out of the deque at most once. This ensures true linear time complexity.
# Space Complexity: O(K) auxiliary space. The mon_deque holds at most K indices at any given moment to manage elements 
# within the active window boundaries.

