class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=len(nums)
        k=len(set(nums))
        if k<s:
            return True
        else: return False
            
