class Solution:
    def countBits(self, n: int) -> List[int]:
        k=[]
        p=[]
        for i in range(n+1):
            k.append(str(bin(i)))
        for i in range(len(k)):
            p.append(k[i].count('1'))
        print(k)
        return p
