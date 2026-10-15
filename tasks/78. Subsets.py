# Task description:
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# Backtracking (State-Space Power Set Generation)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start_index: int, current_subset: list[int]):
            # Every state reached in the decision tree is a valid subset,
            # so we append a deep copy of the current combination to the result
            result.append(current_subset[:])

            # Explore all possible choices moving forward from 'start_index'
            for i in range(start_index, len(nums)):
                # 1. Choose: Include the current element in the subset
                current_subset.append(nums[i])

                # 2. Explore: Recurse deeper into the tree with the next available elements
                backtrack(i + 1, current_subset)

                # 3. Unchoose: Backtrack by removing the element before trying the next branch
                current_subset.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 1
    input_nums = [1, 2, 3]
    power_set = sol.subsets(input_nums)

    print(f"Input Array: {input_nums}")
    # Input Array: [1, 2, 3]
    print(f"Total subsets generated (2^N): {len(power_set)}")
    # Total subsets generated (2^N): 8
    print(power_set)
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]] (order may vary)


# Time Complexity: O(N*2^N), where N is the length of the nums array. A set of size N has exactly 2^N possible subsets.
# For each generated subset, making a deep copy of the current_subset list takes up to O(N) operations in the worst
# case, giving a total time complexity of N*2^N.
# Space Complexity: O(N) auxiliary space. If we exclude the memory space allocated for the final result list, 
# the auxiliary space used is bounded by the recursion call stack depth and the current_subset tracker, both of which 
# grow to a maximum concurrent depth of N.
