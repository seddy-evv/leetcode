# Task Description
# Given an array of integers nums(not sorted) and an integer target, return indices of the two numbers such that they
# add up to target. You may assume that each input would have exactly one solution, and you may not use the same
# element twice. You can return the answer in any order. 

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (Because nums[0] + nums[1] == 9)


# Two-Sum approach:
def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}  # val -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


if __name__ == "__main__":
    # Example execution
    print(twoSum([2, 7, 11, 15], 9))
    # [0, 1]


# Complexity Analysis
#  - Time Complexity: O(n) – We traverse the list containing n elements only once. Each lookup in
#    the HashMap takes O(1) time.
#  - Space Complexity: O(n) – In the worst case, the HashMap will store up to n elements if no matching pair is
#    found until the end.
