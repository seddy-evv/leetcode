# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The elevation map above is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of
# rain water (blue sections) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9


# Two Pointers Approach (Dynamic Programming and Monotonic Stacks are also viable, but Two Pointers is space-optimal)
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            # The smaller height dictates how much water can safely be trapped
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    # Update the maximum wall on the left side
                    left_max = height[left]
                else:
                    # Water is trapped because current height is below left_max
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    # Update the maximum wall on the right side
                    right_max = height[right]
                else:
                    # Water is trapped because current height is below right_max
                    total_water += right_max - height[right]
                right -= 1

        return total_water


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = Solution()
    res = sol.trap(height)
    print(res)
    # 6

# Complexity Analysis:
# Time Complexity: O(n), where n is the number of elements in the height array. The left and right
# pointers travel towards each other and visit each element exactly once.
# Space Complexity: O(1) auxiliary space. The calculation runs entirely in-place utilizing only primitive scalar
# tracking variables.
