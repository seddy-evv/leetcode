# Task Description
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.

# Examples:
# Input: nums = [1, 2, 3, 1] → Output: true
# Input: nums = [1, 2, 3, 4] → Output: false


# The optimal approach uses a Hash Set to track seen numbers in O(n) time.

def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# OR

def containsDuplicateShort(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    # Example execution
    print(containsDuplicate([1, 2, 3, 1]))
    # True
    print(containsDuplicateShort([1, 2, 3, 1]))
    # True

# Complexity Analysis
#  - Time Complexity: O(n) – We traverse the array of n elements once. Set lookup and insertion take O(1) on average.
#  - Space Complexity: O(n) – In the worst case (all unique elements), the set stores all n elements.
