from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        cnt1, cnt2 = Counter(word1), Counter(word2)
        if sorted(cnt1.keys()) == sorted(cnt2.keys()):
            return True if sorted(cnt1.values()) == sorted(cnt2.values()) else False

        return False
        