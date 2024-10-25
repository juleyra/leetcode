class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAlt, highestAlt = 0, 0
        for point in gain:
            currentAlt += point
            if currentAlt > highestAlt:
                highestAlt = currentAlt
        return highestAlt

gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))