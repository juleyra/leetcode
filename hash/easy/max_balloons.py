from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # count, make a dict of letter => count
        # then traverse balloon and check, have a counter a = 0
        # set a = b letter amount,
        checkWord = 'balloon'
        textFrequency = defaultdict(int)
        checkWordFrequency = defaultdict(int)

        for letter in text:
            textFrequency[letter] += 1
        for letter in checkWord:
            checkWordFrequency[letter] += 1

        minCount = float('inf')
        for letter, amount in checkWordFrequency.items():
            minCount = min(minCount, textFrequency[letter] // amount)

        return minCount


text = "nlaebolko"
print(Solution().maxNumberOfBalloons(text))