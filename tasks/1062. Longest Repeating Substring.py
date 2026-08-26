# Task description:
# Given a string s, find out the length of the longest repeating substring(s). A repeating substring is a contiguous
# sequence of characters that appears two or more times in the string. The occurrences of the substring are allowed
# to overlap with each other. If no repeating substring exists, return 0.

# Example 1: Input: s = "abcd" → Output: 0 (No substring repeats).

# Example 2: Input: s = "abbaba" → Output: 2 (The longest repeating substrings are "ab" and "ba", which occur twice).

# Example 3: Input: s = "aaaaa" → Output: 4 (The longest repeating substring is "aaaa", which occurs twice with
# overlapping indices).

# Explanation: By using binary search on the potential lengths of the repeating substring (ranging from 1 to N-1), we
# narrow down the answer space in O(log N) steps. For each length check, a rolling hash function scans the string
# in O(N) time to see if any substring hash appears more than once, avoiding expensive string slices.


# Binary Search on Length with Rolling Hash (Rabin-Karp Algorithm)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)

        # Convert string characters to integers (1-26) for easy rolling hash calculations
        nums = [ord(c) - ord('a') for c in s]

        # Base and Modulo for Rolling Hash (Rabin-Karp)
        # Using a large prime modulo to minimize hash collisions
        base = 26
        mod = 2 ** 63 - 1  # 64-bit integer safe prime

        def search(length: int) -> bool:
            """
            Checks if there is any repeating substring of the given 'length'.
            Uses a rolling hash to check duplicates in O(N) time.
            """
            if length == 0:
                return True

            # Compute the hash of the first window of size 'length'
            current_hash = 0
            for i in range(length):
                current_hash = (current_hash * base + nums[i]) % mod

            # Store seen hashes in a hash set
            seen_hashes = {current_hash}

            # Precompute base^length % mod for efficiently evicting the leftmost element
            base_power = pow(base, length, mod)

            # Slide the window across the rest of the string
            for start in range(1, n - length + 1):
                # Roll hash: Remove leading digit, shift left, add trailing digit
                current_hash = (current_hash * base - nums[start - 1] * base_power + nums[start + length - 1]) % mod

                # If the hash has been seen before, we found a duplicate substring
                if current_hash in seen_hashes:
                    return True
                seen_hashes.add(current_hash)

            return False

        # Binary search space: the repeating substring length must be between 0 and n-1
        left, right = 0, n - 1
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            # If a duplicate substring of length 'mid' exists, try to find a longer one
            if search(mid):
                ans = mid
                left = mid + 1
            else:
                # Otherwise, narrow down the window size
                right = mid - 1

        return ans


if __name__ == "__main__":
    # --- Example Usage ---
    s = "abbaba"
    sol = Solution()
    print(sol.longestRepeatingSubstring(s))
    # 2


# Complexity Analysis:
# Time Complexity: O(NlogN), where N is the length of the string s. The binary search space takes O(log N) splits.
# In each validation step, the search() helper computes a rolling hash across the string length linearly in O(N) time.
# This easily outperforms the basic 2D Dynamic Programming approach which runs in O(N^2).
# Space Complexity: O(N) auxiliary space to maintain the integer conversion array and the seen_hashes set inside the
# window evaluation block.
