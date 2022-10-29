class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=nums.count(val)
        for i in range(k):
            nums.remove(val)
            
        return len(nums)
