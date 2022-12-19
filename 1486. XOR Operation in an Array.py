class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        k=[]
        for i in range(n):
            s=start+2*i
            k.append(s)
        xor=0
        for i in range(len(k)):
            xor=xor^k[i]
        return xor
