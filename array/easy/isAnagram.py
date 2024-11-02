class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countedLetters = {}
        for letter in s:
            countedLetters[letter] = countedLetters.get(letter, 0) + 1
        for letter in t:
            if letter in countedLetters:
                if countedLetters[letter] == 0:
                    return False
                else:
                    countedLetters[letter] = countedLetters.get(letter, 0) - 1
            else:
                return False
        return True