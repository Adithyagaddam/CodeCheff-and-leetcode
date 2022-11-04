class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k=list(jewels)
        r=list(stones)
        count=0
        for i in range(len(k)):
            for j in range(len(r)):
                if k[i]==r[j]:
                    count+=1
        return count
