class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            s.append(nums[nums[i]])
        return s
