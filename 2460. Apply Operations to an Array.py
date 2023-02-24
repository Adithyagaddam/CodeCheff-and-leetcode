class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums
