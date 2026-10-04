# Task description:
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
# a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
# - Trie() Initializes the trie object.
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
# otherwise.
# - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix
# prefix, and false otherwise.

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.


# Trie (Prefix Tree) Node Traversal via Nested Hash Maps.
class TrieNode:
    def __init__(self):
        # A dictionary mapping characters to their corresponding child TrieNodes
        self.children = {}
        # Boolean flag indicating if a complete word terminates at this node
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """Initializes the trie object."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        curr = self.root
        for char in word:
            # If the character node doesn't exist, instantiate a new subtree branch
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # Mark the end node of the word path
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns true if the string word is in the trie, and false otherwise."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # The word only exists if it path-matches completely AND ends at a word termination flag
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns true if there is a previously inserted string word that has the prefix, and false otherwise."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we successfully trace the entire prefix route, a matching prefix exists
        return True


if __name__ == "__main__":
    # Initialize the Prefix Tree structure
    trie = Trie()

    # 1. Insert words
    trie.insert("apple")
    print("Inserted 'apple'")

    # 2. Test exact word matches
    print(f"Search 'apple':     {trie.search('apple')}")  # Output: True
    print(f"Search 'app':       {trie.search('app')}")  # Output: False

    # 3. Test prefix matches
    print(f"StartsWith 'app':   {trie.startsWith('app')}")  # Output: True

    # 4. Insert conflicting shorter word
    trie.insert("app")
    print("Inserted 'app'")
    print(f"Search 'app' now:   {trie.search('app')}")  # Output: True


# Time Complexity:
# 	• insert(word): O(L), where L is the length of the string being inserted. We step through and link at most L
# 	characters.
# 	• search(word): O(L), where L is the length of the look-up string. We perform up to L hash-map key evaluations.
# 	• startsWith(prefix): O(P), where P is the length of the prefix string.
# Space Complexity:
# 	• insert(word): O(L) worst-case space to allocate up to L new TrieNode components if none of the prefix segments
# 	match existing tree branches.
# 	• search(word) & startsWith(prefix): O(1) auxiliary space since characters are evaluated inline using iterative
# 	search pointers without any memory accumulation.
# 	• Overall Structural Footprint: Bounded by O(N*L) worst-case space to hold N total inserted strings of average
# 	length L, heavily optimized by shared overlapping prefixes.
