"""
Given a string s, find the length of the longest  substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        chrs = {}
        result_str = ""
        max = 0
        for i in s:
            count = chrs.get(i, 0)
            if not count:
                result_str += i
                chrs[i] = 1
                if max < len(result_str):
                    max = len(result_str)
            else:
                result_str = (result_str + i)[result_str.index(i) + 1:]
                if max < len(result_str):
                    max = len(result_str)
                chrs = {}
                chrs = dict.fromkeys([*result_str], 1)
        if max < len(result_str):
            max = len(result_str)
        return max
