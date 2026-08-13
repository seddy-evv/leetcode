# The next greater element of some element x in an array is the first greater element that is to the right of x in
# the same array.You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
# element of nums2[j] in nums2. If there is no next greater element, the answer for this query is -1.Return an array
# ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
#   For number 4 in nums1: The next greater element to the right of 4 in nums2 does not exist, so output -1.
#   For number 1 in nums1: The next greater element to the right of 1 in nums2 is 3.
#   For number 2 in nums1: The next greater element to the right of 2 in nums2 does not exist, so output -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]


# Monotonic Stack (combined with a Hash Map for fast index mapping)
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Hash map to map an element from nums2 to its next greater element
        next_greater_map = {}
        # Monotonic decreasing stack
        stack = []

        # Traverse nums2 to precalculate next greater elements
        for num in nums2:
            # While the stack is not empty and the current number is greater
            # than the element at the top of the stack
            while stack and num > stack[-1]:
                popped_element = stack.pop()
                next_greater_map[popped_element] = num

            # Push the current number onto the stack
            stack.append(num)

        # Build the final result array for nums1 using our precalculated map
        # Using .get(num, -1) defaults to -1 if no greater element was found
        return [next_greater_map.get(num, -1) for num in nums1]


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 0, 3, 4, 2]
    sol = Solution()
    res = sol.nextGreaterElement(nums1, nums2)
    print(res)
    # [-1, 3, -1]

# Complexity Analysis:
# Time Complexity: O(n + m), where n is the length of nums2 and m is the length of nums1. Even though
# there is a nested while loop, every single element is pushed onto the stack exactly once and popped from the stack
# at most once, keeping the operation strictly linear.
# Space Complexity: O(n) to store the elements inside the stack tracking buffer and the next_greater_map hashing
# container.
