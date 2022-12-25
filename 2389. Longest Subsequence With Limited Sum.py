class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    
        s=[]

        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for i in queries:
            index = bisect.bisect_right(nums, i)
            s.append(index)
        return s
