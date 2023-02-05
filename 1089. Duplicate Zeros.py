class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k=len(arr)
        i=0
        while(i<k):
            if arr[i]==0:
                arr.insert(i,0)
                i=i+2
                arr.pop()
            else:
                i=i+1
