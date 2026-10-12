# Task description:
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result
# of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
# such as eval().

# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


# Stack-Based Linear Expression Parsing with Sign-State Preservation
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_result = 0
        current_sign = 1  # 1 represents positive (+), -1 represents negative (-)
        i = 0
        n = len(s)

        while i < n:
            char = s[i]

            if char.isdigit():
                # Formulate multi-digit numbers iteratively
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # Apply the current active sign to the fully parsed number
                current_result += current_sign * num
                # Adjust pointer backward by 1 because the main loop increments it
                i -= 1

            elif char == '+':
                current_sign = 1

            elif char == '-':
                current_sign = -1

            elif char == '(':
                # Push the running result and active sign state onto the stack
                # before entering the parenthetical sub-problem
                stack.append(current_result)
                stack.append(current_sign)
                # Reset local state parameters for the nested evaluation context
                current_result = 0
                current_sign = 1

            elif char == ')':
                # Sub-problem resolved. Pop the sign context that preceded '('
                prev_sign = stack.pop()
                prev_result = stack.pop()

                # Update total running score combining the newly resolved inner scope
                current_result = prev_result + (prev_sign * current_result)

            i += 1

        return current_result


if __name__ == "__main__":
    sol = Solution()

    # Test expression containing spaces and parenthetical loops
    expression = "(1+(4+5+2)-3)+(6+8)"
    result = sol.calculate(expression)

    print(f"Expression:        {expression}")
    # Expression: (1 + (4 + 5 + 2) - 3) + (6 + 8)
    print(f"Calculated Result: {result}")
    # Calculated Result: 23


# Time Complexity: O(N), where N is the length of the string s. The algorithm scans the input string in a single linear
# pass. The inner while loop advances the primary pointer index continuously without processing any index character
# more than once.
# Space Complexity: O(N) auxiliary space. In the worst-case scenario where the expression contains deeply nested
# opening parentheses (e.g., (((((1+1))))))), the stack tracks up to \(\mathcal{O}(N)\) snapshot states concurrently
# before resolving the inner scopes.
