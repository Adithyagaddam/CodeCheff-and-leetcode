class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        t=format(start,'032b')
        s=format(goal,'032b')
        k=str(t)
        p=str(s)
        l=[x for x in k ]
        q=[x for x in p]
        count=0
        for i in range(len(l)):
            if l[i]!=q[i]:
                count+=1
        return count
