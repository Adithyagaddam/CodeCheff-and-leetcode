class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            tmp = [ele[i] for ele in strs]
            tmp_sort = sorted(tmp)
            if tmp !=tmp_sort:
                count+=1
        return count
