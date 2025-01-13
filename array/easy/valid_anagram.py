from collections import defaultdict
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = Counter(s)
        print(a)
        # counter = defaultdict(list)
        # for l in s:
        #     counter[l] = counter.get(l, 0) + 1
        # for l in t:
        #     if l not in counter:
        #         return False
        #     counter[l] = counter.get(l, 0) - 1
        # for amount in counter.values():
        #     if amount !=0:
        #         return False
        # return True





s = "anagram"
t = "nagaram"
a = Solution().isAnagram(s, t)
print(a)