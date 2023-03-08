class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        t=0
        while len(nums)>1:
            p=str(nums[0])+str(nums[-1])
            t+=int(p)
            del nums[0]
            del nums[-1]
            
        if len(nums)==1:
            t+=nums[0]
        return t
