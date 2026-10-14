# Task description:
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
# beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
# transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# Breadth-First Search (BFS) with Generic Intermediate State Preprocessing.
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # If the destination word is not in the dictionary, no valid sequence exists
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # Preprocess the dictionary into a generic intermediate state mapping
        # E.g., "hot" maps to templates: "*ot", "h*t", "ho*"
        combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                generic_word = word[:i] + "*" + word[i + 1:]
                combo_dict[generic_word].append(word)

        # Queue for standard BFS traversal tracking: (current_word, level_steps)
        queue = deque([(beginWord, 1)])

        # Visited set to prevent cyclic loops
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            # For every character slot, generate the corresponding generic template
            for i in range(L):
                generic_word = current_word[:i] + "*" + current_word[i + 1:]

                # Retrieve all adjacent words matching this template layout
                for next_word in combo_dict[generic_word]:
                    # Target reached successfully
                    if next_word == endWord:
                        return level + 1

                    # If the word hasn't been visited yet, enqueue it
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

                # Optimization step: clear the combinations list once visited
                # to prevent redundant lookup paths later
                combo_dict[generic_word] = []

        return 0


if __name__ == "__main__":
    sol = Solution()

    start_word = "hit"
    target_word = "cog"
    dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]

    steps = sol.ladderLength(start_word, target_word, dictionary)
    print(f"Begin Word: '{start_word}', End Word: '{target_word}'")
    # Begin Word: 'hit', End Word: 'cog'
    print(f"Shortest transformation path distance: {steps}")
    # Shortest transformation path distance: 5


# Time Complexity: O(M^2*N)\), where M is the fixed length of each word and N is the total number of words in
# the wordList. Preprocessing the dictionary maps takes O(M^2*N) time because for each of the N words, we iterate
# M times to create a string slice of length M. The BFS loop visits at most N words, evaluating M intermediate
# templates of length M for each node, yielding a matching runtime.
# Space Complexity: O(M^2*N) auxiliary space required to maintain the combo_dict map structure holding intermediate
# string representations. The visited tracking set and queue allocate additional structures bounded linearly
# by O(M*N).
