import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k=int((num)**0.5)
        s=(k*k)
        if s==num:
            return True
