class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            s=str(nums[i])
            if len(s)%2==0:
                count+=1
        return count
