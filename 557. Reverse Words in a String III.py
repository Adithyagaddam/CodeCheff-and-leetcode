class Solution:
    def reverseWords(self, s: str) -> str:
        k=[i for i in s.split()]
        print(k)
        r=[]
        for i in range(len(k)):
            x=k[i][::-1]
            r.append(x)
        return(' '.join(r))
        
