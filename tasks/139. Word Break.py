# Task description:
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


# Dynamic Programming (Bottom-Up Tabulation).
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Convert the word dictionary to a set for O(1) fast lookups
        word_set = set(wordDict)

        # dp[i] will be True if the substring s[0:i] can be segmented
        dp = [False] * (len(s) + 1)

        # Base case: An empty string is always a valid segmentation
        dp[0] = True

        # Iterate through all possible lengths of the substring
        for i in range(1, len(s) + 1):
            # Check all possible split points before index i
            for j in range(i):
                # If s[0:j] is valid and the remaining part s[j:i] is in the word set
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split point for i, move to the next length

        return dp[len(s)]


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))
    # Output: True
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # Output: False


# Time Complexity: O(N^3) in the worst case, where N is the length of the string s. There are two nested loops
# contributing O(N^2), and inside the loop, the string slicing operation s[j:i] takes up to O(N) time.
# (Note: In practice, this can be optimized to O(N*M) where M is the maximum length of a word in wordDict by limiting
# j to go back only up to M characters).
# Space Complexity: O(N + W) auxiliary space, where N is the length of string s for the boolean dp tracking table
# and W is the total memory used to store the dictionary inside word_set.
