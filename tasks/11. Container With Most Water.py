# Task description:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
# water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


# Two-Pointer Technique.
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # The width of the container is the distance between the two pointers
            width = right - left

            # The height of the water is limited by the shorter of the two lines
            current_height = min(height[left], height[right])

            # Calculate the volume of water for the current container
            current_water = width * current_height

            # Update the maximum water found so far
            max_water = max(max_water, current_water)

            # Move the pointer pointing to the shorter line inward
            # This is because a longer line might give a larger area despite the decreasing width
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # Output: 49


# Complexity Analysis:
# ime Complexity: O(N), where N is the length of the height array. The left and right pointers start at opposite ends
# and move closer together by one step per iteration, looking at each element at most once.
# Space Complexity: O(1) auxiliary space, as the tracking variables (left, right, max_water, etc.) consume constant
# memory.
