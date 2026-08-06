# Design an algorithm to encode a list of strings to a single consolidated string. This encoded string is then sent
# over a network and must be decoded back into the original list of strings.
# Please implement encode and decode methods.

# Example 1:
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation: Your encode method can convert it to any format (e.g., "5#Hello5#World"). The decode method must be
# able to restore it exactly.

# Example 2:
# Input: dummy_input = [""]
# Output: [""]


# Length-Prefixed Framing (Chunk Encoding)
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_chunks = []
        for s in strs:
            # Append the length of the string, the delimiter, and the string itself
            encoded_chunks.append(f"{len(s)}#{s}")
        return "".join(encoded_chunks)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0

        while i < len(s):
            # Find where the delimiter '#' is to parse the preceding length integer
            j = i
            while s[j] != '#':
                j += 1

            # Extract the length of the upcoming string
            length = int(s[i:j])

            # Slice out the string based on the extracted length
            # The string starts right after '#' (j + 1) and ends at (j + 1 + length)
            start_index = j + 1
            end_index = start_index + length
            res.append(s[start_index:end_index])

            # Move the pointer 'i' to process the next encoded chunk
            i = end_index

        return res


if __name__ == "__main__":

    sol = Codec()
    input = ["Hello", "World"]
    encoded_output = sol.encode(input)
    print(encoded_output)
    # 5#Hello5#World
    print(sol.decode(encoded_output))
    # ['Hello', 'World']


# Complexity Analysis:
# Time Complexity:
# encode: O(n), where n is the total number of characters across all strings.
# decode: O(n), as we process the single combined string linearly from start to finish.
# Space Complexity:
# encode: O(n) to construct and return the new string.
# decode: O(n) to hold the list of newly reconstructed strings.
