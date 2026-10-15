# Task description:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


# Backtracking (State-Space Combinatorial Tree Search).
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Return an empty list immediately if the input string is empty
        if not digits:
            return []

        # Keypad map representing telephone digit configurations
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, current_path: list[str]):
            # Base Case: If the path length matches the digits string length,
            # we have formed a complete combination.
            if len(current_path) == len(digits):
                result.append("".join(current_path))
                return

            # Fetch the mapped letters for the current digit character
            current_digit = digits[index]
            letters = phone_map[current_digit]

            # Explore decisions
            for letter in letters:
                # 1. Choose: Append the character to our active state path
                current_path.append(letter)

                # 2. Explore: Recurse deeper into the tree for the next digit index
                backtrack(index + 1, current_path)

                # 3. Unchoose: Backtrack by popping the last character out
                current_path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 1
    digit_input = "23"
    combinations = sol.letterCombinations(digit_input)

    print(f"Input Digits: '{digit_input}'")
    # Input Digits: '23'
    print(f"Total combinations generated: {len(combinations)}")
    # Total combinations generated: 9
    print(f"Combinations: {combinations}")
    # Combinations: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


# Time Complexity: O(4^N*N), where N is the length of the digits string. A single digit button can map up to 4
# characters (e.g., keys 7 and 9). In the worst-case layout, the tree expands up to 4^N unique combination leaf nodes.
# At each leaf node, joining the structural characters into a finalized string wrapper takes up to O(N) steps.
# Space Complexity: O(N) auxiliary space. If we exclude the memory slots needed to pass the finalized list of output
# strings, the extra memory is bounded tightly by the maximum operational depth of the recursion stack frame layers,
# which scales linearly up to N levels.
