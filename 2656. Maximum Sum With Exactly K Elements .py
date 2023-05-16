class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum=0
        for i in range(k):
            sum+=max(nums)
            nums[-1]=max(nums)+1
        return sum
