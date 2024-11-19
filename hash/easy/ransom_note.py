from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # count magazine letters amount
        # traverse ransom note, and decrement letter amount
        # if no such letter or amount is not enough - return False
        # return true after otherwise

        freq = defaultdict(int)
        for l in magazine:
            freq[l] += 1
        for l in ransomNote:
            if not freq[l]:
                return False
            freq[l] -=1

        return True


ransomNote = 'aaddd'
magazine = 'aab'
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))