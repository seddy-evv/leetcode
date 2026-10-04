# Task description:
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.

# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.


# Trie (Prefix Tree) with Backtracking Depth-First Search (DFS) for Wildcard Matching.
class TrieNode:
    def __init__(self):
        # A dictionary mapping characters to child TrieNodes
        self.children = {}
        # Flag indicating if a complete word terminates at this node
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        """Initializes the object."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds a word to the data structure."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns true if there is any string matching word, including '.' wildcards."""

        def dfs(index: int, node: TrieNode) -> bool:
            curr = node
            for i in range(index, len(word)):
                char = word[i]

                if char == '.':
                    # Wildcard branch: Try matching all existing child nodes recursively
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # Regular character path evaluation
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

            return curr.is_end_of_word

        return dfs(0, self.root)


if __name__ == "__main__":
    # Initialize the Word Dictionary data structure
    word_dict = WordDictionary()

    # 1. Add sample words
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print("Added words: 'bad', 'dad', 'mad'")

    # 2. Search exact matches
    print(f"Search 'pad': {word_dict.search('pad')}")  # Output: False
    print(f"Search 'bad': {word_dict.search('bad')}")  # Output: True

    # 3. Search using wildcards
    print(f"Search '.ad': {word_dict.search('.ad')}")  # Output: True (Matches 'bad', 'dad', or 'mad')
    print(f"Search 'b..': {word_dict.search('b..')}")  # Output: True (Matches 'bad')
    print(f"Search '..x': {word_dict.search('..x')}")  # Output: False


# Time Complexity:
# 	• addWord(word): O(L), where L is the length of the word being added. The algorithm traverses or allocates at
# 	most L nodes linearly.
# 	• search(word): O(M) in the worst case where no wildcards are present (where M is the search string length).
# 	However, if wildcards '.' are included, it branches out. In the absolute worst case (e.g., searching ... on
# 	a dictionary filled with combinations), it can explore up to O(N*Σ^M) nodes where Σ is the alphabet size (26) and
# 	N is the total node footprint.
# Space Complexity:
# 	• addWord(word): O(L) worst-case space to instantiate new TrieNode instances if the word shares no existing
# 	prefixes.
# 	• search(word): O(M) auxiliary space consumed by the recursive DFS function's stack allocation depth, which is
# 	directly bounded by the search string length M.
