class Solution(object):
    def groupAnagrams(self, strs):
        # Create an empty dictionary to store groups of anagrams
        anagram_groups = {}

        # Iterate through each word in the input list of strings
        for word in strs:
            # Sort the letters of the word to get its "canonical" form
            sorted_word = ''.join(sorted(word))

            # Check if the sorted word exists as a key in the dictionary
            if sorted_word in anagram_groups:
                # If it exists, append the original word to the list of anagrams
                anagram_groups[sorted_word].append(word)
            else:
                # If it doesn't exist, create a new key with the sorted word and set its value as a list containing the original word
                anagram_groups[sorted_word] = [word]

        # Return the values of the dictionary, which are lists of anagrams
        return list(anagram_groups.values())



        