class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        k=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                k.append(nums[i])
        print(k)
        return sum(k)
