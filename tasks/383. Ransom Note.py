"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        magazine_dict = {}
        for ch in ransomNote:
            ransom_dict[ch] = ransom_dict.get(ch, 0) + 1
        for ch in magazine:
            magazine_dict[ch] = magazine_dict.get(ch, 0) + 1
        for key, value in ransom_dict.items():
            if value > magazine_dict.get(key, 0):
                return False
        return True
