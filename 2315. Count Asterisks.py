class Solution:
    def countAsterisks(self, s: str) -> int:
        n = len(s)
        res = 0
        isPair = False 
        
        for i in range(n):
            
            if not isPair and s[i] == "*":
                res += 1
            if s[i] == "|":
                isPair = not isPair
                
        return res
