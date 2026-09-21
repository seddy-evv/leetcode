# Task description:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# Constraints:
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# Patience Sorting with Binary Search (also known as the bisect / Tail Table Optimization approach)
import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # This list will store the smallest tail element of all
        # increasing subsequences discovered so far
        sub = []

        for num in nums:
            # Use binary search to find the correct insertion index for 'num'
            idx = bisect.bisect_left(sub, num)

            # If num is larger than all elements in sub, append it to extend the sequence
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the element at idx with num to optimize future subproblems
            else:
                sub[idx] = num

        return len(sub)


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # Output: 4


# Time Complexity: O(NlogN), where N is the length of the nums array. We make a single linear pass over the array,
# and during each of the N steps, we perform a binary search lookup using bisect_left which runs in O(log N) time.
# Space Complexity: O(N) auxiliary space to store the monotonic sequence elements inside the tracking list sub in
# a worst-case scenario where the array is already perfectly sorted.
