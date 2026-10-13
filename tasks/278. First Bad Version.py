# Task description:
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all
# the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# Constraints:
# 1 <= bad <= n <= 231 - 1


# Binary Search (Boundary Finding Variant).
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            # Prevents potential integer overflow
            mid = low + (high - low) // 2

            # If mid is a bad version, the first bad version could be mid or to its left
            if isBadVersion(mid):
                high = mid
            # If mid is not a bad version, the first bad version must be strictly to its right
            else:
                low = mid + 1

        # When low == high, it points directly to the first bad version
        return low


# --- Mocking the LeetCode environment API for local testing ---
FIRST_BAD_VERSION = 4


def isBadVersion(version: int) -> bool:
    """Mock API helper."""
    return version >= FIRST_BAD_VERSION


if __name__ == "__main__":
    sol = Solution()

    total_versions = 5
    result = sol.firstBadVersion(total_versions)

    print(f"Total versions: {total_versions}, Secret first bad version: {FIRST_BAD_VERSION}")
    print(f"First bad version detected by algorithm: {result}")
    # Output: 4


# Time Complexity: O(log N), where N is the total number of versions n. The search space is divided strictly in half
# during each iteration, minimizing the number of expensive isBadVersion API lookups to a logarithmic scale.
# • Space Complexity: O(1) constant auxiliary space. The traversal tracks boundaries in-place using only basic
# scalar integer markers (low, high, and mid).
