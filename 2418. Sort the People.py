class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t=zip(names,heights)
        s=[]
        for names,heights in t:
            s.append([names,heights])
        s.sort(key = lambda x: x[1],reverse=True)
        t=[]
        for i in range(len(s)):
            t.append(s[i][0])
        return t
