"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-2**31 <= x <= 2**31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            positive = False
        else:
            positive = True
        x = abs(x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10

        if positive:
            res = res
        else:
            res = -res
        if res > 2**31 - 1 or res < -2**31:
            res = 0
        return res
