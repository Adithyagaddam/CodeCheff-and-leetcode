class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0
        l=len(nums)
        while x<l-1:
            if nums[x]==nums[x+1]:
                nums.remove(nums[x+1])
            else:
                x+=1
            l=len(nums)
        return len(nums)
