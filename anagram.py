class Solution(object):
    def isAnagram(self, s, t):
        # Check if lengths are different
        if len(s) != len(t):
            return False

        # Count characters in both strings
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1

        # Check if all counts are 0
        for count in char_count.values():
            if count != 0:
                return False

        return True


        