class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        for i in range(len(accounts)):
            k = sum(accounts[i])
            s=max(s,k) 
        return s
            
