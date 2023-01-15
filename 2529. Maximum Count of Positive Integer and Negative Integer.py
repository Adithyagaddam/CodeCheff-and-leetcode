class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        con=0
        for i in range(len(nums)):
            if nums[i]>0:
                count+=1
            elif nums[i]<0:
                con+=1
        return max(count,con)
