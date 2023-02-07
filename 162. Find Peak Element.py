class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)>1:
            k=max(nums)
            return (nums.index(k))
        else: return 0
