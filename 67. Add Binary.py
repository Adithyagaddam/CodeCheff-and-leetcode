from operator import*
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        sum=sum[2:]
        return sum
        
