#  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
#  non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
#  numbers.

#  Given a string s, return true if it is a palindrome, or false otherwise.
#  Example 1:
#  Input: s = "A man, a plan, a canal: Panama"
#  Output: true
#  Explanation: "amanaplanacanalpanama" is a palindrome.

#  Example 2:
#  Input: s = "race a car"
#  Output: false
#  Explanation: "raceacar" is not a palindrome.

#  Example 3:
#  Input: s = " "
#  Output: true
#  Explanation: s becomes an empty string "" after removing non-alphanumeric characters. Since an empty string reads
#  the same forward and backward, it is a palindrome.


# Two Pointers Technique
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters in lowercase
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers closer to the center
            left += 1
            right -= 1

        return True


if __name__ == "__main__":

    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(sol.isPalindrome("race a car"))  # Output: False
    print(sol.isPalindrome(" "))  # Output: True


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the string s. Each character is visited at most a constant number
# of times as the pointers move toward each other.
# Space Complexity: O(1) because the algorithm operates entirely in-place using only index pointers, requiring no
# extra memory allocations.

# Using s[::-1] (or any filtering like "".join(...)) creates a brand-new string copy in memory. This forces the space
# complexity up to O(n).
