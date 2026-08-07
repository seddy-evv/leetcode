# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does
# not exist.
# An alphanumeric string consists of lowercase English letters and digits.
# Example 1:
# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits present in s are ['1', '2', '3']. The largest digit is 3, and the second largest digit is 2.

# Example 2:
# Input: s = "abc1111"
# Output: -1
# Explanation: The only digit present in s is 1. There is no second largest digit.


# One-Pass Linear Scan with Character Filtering
class Solution:
    def secondHighest(self, s: str) -> int:
        first_max = None
        second_max = None

        for char in s:
            # Filter out alphabet letters, keep only digits
            if char.isdigit():
                num = int(char)

                # Case 1: Found a new absolute highest digit
                if first_max is None or num > first_max:
                    second_max = first_max
                    first_max = num
                # Case 2: Found a digit smaller than first_max, but potentially larger than second_max
                elif num < first_max:
                    if second_max is None or num > second_max:
                        second_max = num

        # Return second_max if it was found, otherwise return -1
        return second_max if second_max is not None else -1


if __name__ == "__main__":

    sol = Solution()
    s = "dfa12321afd"
    print(sol.secondHighest(s))
    # 2
    s = "abc1111"
    print(sol.secondHighest(s))
    # -1


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of string s. We traverse the string exactly once.
# Checking .isdigit() and updating variables takes O(1) time.
# Space Complexity: O(1) auxiliary space. We only store two integer pointers (first_max and second_max),
# which requires no extra structural memory.
