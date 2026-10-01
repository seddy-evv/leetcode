# Task description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# Stack-Based Linear Parsing (Last-In, First-Out / LIFO).
class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening pairs
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the opening bracket matches the required pair
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # The string is valid only if all opening brackets have been matched and popped
        return len(stack) == 0


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # Output: True
    print(sol.isValid("(]"))  # Output: False


# Time Complexity: O(N), where N is the length of the string s. We iterate through the string exactly once. Each
# character involves a stack push or pop operation, which runs in constant O(1) time.
# Space Complexity: O(N) auxiliary space. In the worst-case scenario (e.g., input string consists entirely of opening
# brackets like "(((((["), the stack will hold all N characters.
