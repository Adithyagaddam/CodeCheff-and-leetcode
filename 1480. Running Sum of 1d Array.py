class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        k=0
        for i in range(len(nums)):
            k=nums[i]+k
            a.append(k)
        return a
        
