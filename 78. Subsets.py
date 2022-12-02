class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = []
        for i in range(len(nums)+1):
            lists += [list(j) for j in combinations(nums, i)]
        return lists
