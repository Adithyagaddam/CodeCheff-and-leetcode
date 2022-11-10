class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        s=len(nums)
        if s>=3:
            r=nums[s-3]
        elif s==2:
            r=nums[1]
        else:
            r=nums[0]
              
        return r
