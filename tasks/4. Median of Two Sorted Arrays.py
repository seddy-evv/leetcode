# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)).
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Binary Search on Partitions
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search runtime to O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_half = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:
            # Partition point for nums1
            i = (low + high) // 2
            # Partition point for nums2 derived from total_half requirement
            j = total_half - i

            # Find elements immediately around the partition boundaries
            # Handle out-of-bound edge cases using infinity sentinels
            left1 = nums1[i - 1] if i > 0 else -float('inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else -float('inf')
            right2 = nums2[j] if j < n else float('inf')

            # Check if we found the correct partition alignment
            if left1 <= right2 and left2 <= right1:
                # If total elements count is odd
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # If total elements count is even
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            # If left1 is too big, we must shift the partition boundary of nums1 to the left
            elif left1 > right2:
                high = i - 1
            # If left2 is too big, we must shift the partition boundary of nums1 to the right
            else:
                low = i + 1

        return 0.0


if __name__ == "__main__":

    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))
    # 2.0


# Complexity Analysis:
# Time Complexity: O(log(min(m, n))), where m and n are the lengths of the two arrays. Since the
# binary search runs exclusively on the smaller array, it strictly satisfies the O(log(m+n)) requirement.
# Space Complexity: O(1) auxiliary space. The algorithm tracks index pointers and bounds entirely in-place
# without copying or merging elements.
