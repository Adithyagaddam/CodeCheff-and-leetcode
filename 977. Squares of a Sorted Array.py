class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            s=nums[i]**2
            k.append(s)
        k.sort()
        return k
