class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s=Counter(words1)
        t=Counter(words2)
        for j,l in s.most_common():
            if l>1:
                for i in range(l):
                    words1.remove(j)
        for j,l in t.most_common():
            if l>1:
                for i in range(l):
                    words2.remove(j)
        count=0
        for i in words1:
            if i in words2:
                count+=1
        return count
