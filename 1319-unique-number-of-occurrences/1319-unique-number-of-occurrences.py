from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = list(Counter(arr).values())
        return len(freq) == len(set(freq))





        