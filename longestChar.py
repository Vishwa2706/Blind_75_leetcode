class Solution(object):
    def characterReplacement(self, s, k):
        if not s:
            return 0

        max_length = 0
        max_count = 0
        char_count = {}

        left = 0
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            # If the length of the window exceeds the number of replacements allowed,
            # we need to shrink the window from the left side.
            if right - left + 1 - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length





        