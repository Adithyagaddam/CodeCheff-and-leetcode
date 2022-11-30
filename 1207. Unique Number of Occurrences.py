from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=Counter(arr)
        if len(set(s.values()))==len(s.values()):
            return True
