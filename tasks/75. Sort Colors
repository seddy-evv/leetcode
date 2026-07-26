# Task Description
# Sort an array nums of n objects (0s, 1s, 2s) in-place so colors are adjacent, ordered as red (0), white (1),
# and blue (2). You cannot use built-in sorting and must aim for a one-pass, O(1) space solution.

# Examples: [2,0,2,1,1,0] -> [0,0,1,1,2,2].
# Constraints: 1 <= n <= 300.

# Dutch National Flag algorithm:

def sortColors(nums: list[int]) -> list:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else: # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


if __name__ == "__main__":
    print(sortColors([2, 0, 2, 1, 1, 0]))
    # [0, 0, 1, 1, 2, 2]

Time: O(N) (single pass).
Space: O(1) (in-place).
