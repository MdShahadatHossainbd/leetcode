class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(letter.islower() for letter in word):
            return True
        elif all(letter.isupper() for letter in word):
            return True
        elif word[0].isupper() and all(letter.islower() for letter in word[1:]):
            return True
        else:
            return False

