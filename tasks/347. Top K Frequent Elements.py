# Task description:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer
# in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# Bucket Sort (Frequency-Indexed Array Grouping).
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each number
        counts = Counter(nums)

        # Step 2: Create a bucket array where the index represents the frequency.
        # The maximum possible frequency of an element is len(nums).
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        # Step 3: Iterate backward from the highest frequency bucket to gather top K elements
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                # Once we have collected k elements, return the result early
                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test Case matching Example 1
    nums_input = [1, 1, 1, 2, 2, 3]
    k_value = 2

    output = sol.topKFrequent(nums_input, k_value)
    print(f"The top {k_value} frequent elements are: {output}")
    # Output: [1, 2]


# Time Complexity: O(N), where N is the total number of elements in the nums array. Populating the frequency count
# hash map takes O(N) time. Distributing elements into the bucket positions takes O(U) time where U <= N is the number
# of unique elements. Gathering the final result by checking the buckets takes at most O(N) steps, yielding an overall
# linear runtime.
# Space Complexity: O(N) auxiliary space. The counts map tracks unique entries bounded by N, and the buckets
# collection spans an allocated length of len(nums) + 1 to accommodate all possible frequency values.
