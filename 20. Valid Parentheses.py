class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        for i in range(len(s)):
            if s.count("(")==s.count(")") and s.count("[")==s.count("]") and s.count("{")==s.count("}"):
                return True
