# Task description:
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


# Two-Pointer Bitwise Addition Simulation (Schoolbook Addition Pattern).
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Initialize pointers at the end of both strings (least significant bits)
        i = len(a) - 1
        j = len(b) - 1

        # Loop as long as there are characters left to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # The current bit value is total % 2 (either 0 or 1)
            result.append(str(total % 2))
            # The new carry value is total // 2 (1 if total >= 2, else 0)
            carry = total // 2

        # Reverse the accumulated bits to form the correct most-significant-to-least order
        return "".join(reversed(result))


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 matching Example 1
    str_a1 = "11"
    str_b1 = "1"
    print(f"Sum of '{str_a1}' and '{str_b1}': {sol.addBinary(str_a1, str_b1)}")
    # Sum of '11' and '1': 100

    # Test Case 2 matching Example 2
    str_a2 = "1010"
    str_b2 = "1011"
    print(f"Sum of '{str_a2}' and '{str_b2}': {sol.addBinary(str_a2, str_b2)}")
    # Sum of '1010' and '1011': 10101


# Time Complexity: O(max(N, M)), where N is the length of string a and M is the length of string b. The algorithm
# runs a single backward loop proportional to the length of the longer string, performing O(1) basic arithmetic
# operations on each iteration.
# Space Complexity: O(max(N, M)) auxiliary space required to build the result string buffer. The final string can
# hold at most max(N, M) + 1 character tokens.
