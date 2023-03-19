class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        t=Counter(nums)
        s=[]
        for j,l in t.most_common():
            s.append(l)
        r=[]
        p=[]
        l=[]
        for i in range(len(s)):
            if s[i]%2==0:
                r.append(int(s[i]/2))   
            elif s[i]%2!=0:
                r.append(s[i]//2)
                p.append(1)
        l.append(sum(r))
        l.append(sum(p))
        return l
