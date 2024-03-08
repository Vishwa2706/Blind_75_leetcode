class LongestSubstring:
    def length_of_longest_substring(self, s: str) -> int:
        # Initialize variables
        max_length = 0
        start = 0
        char_index_map = {}

        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is already in the map and its index is after the start position,
            # update the start position to the next index of the repeating character.
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            # Update the index of the current character in the map
            char_index_map[char] = i

            # Update the maximum length if the current substring is longer
            max_length = max(max_length, i - start + 1)

        return max_length

# Example usage:
substring_finder = LongestSubstring()
s = "abcabcbb"
print(substring_finder.length_of_longest_substring(s))  # Output: 3 (The longest substring without repeating characters is "abc")
