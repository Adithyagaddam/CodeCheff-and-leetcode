class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        for i in range(len(candies)):
            s=candies[i]+extraCandies
            if s>=max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
        
