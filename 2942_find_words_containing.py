from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Initialize a list to store the indices of words containing the character x
        word_character = []

        # Iterate through each word in the list by index
        for i in range(len(words)):
            # Check if the character x is present in the current word
            if x in words[i]:
                # If found, append the index to the result list
                word_character.append(i)

        # Return the list of indices
        return word_character
