class Solution:
    def countEven(self, num: int) -> int:
        s=[]
        for i in range(1,num+1):
            s.append(i)
        p=[]
        for i in range(len(s)):
            k=str(s[i])
            p.append(sum([int(x) for x in k]))
        count=0
        for i in range(len(p)):
            if p[i]%2==0:
                count+=1
        return count
