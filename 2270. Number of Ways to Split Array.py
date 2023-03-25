class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        sm=sum(nums)
        lsm=0
        for i in  range(len(nums)-1):
            sm-=nums[i]
            lsm+=nums[i]
            if lsm>=sm:
                count+=1
        return count
