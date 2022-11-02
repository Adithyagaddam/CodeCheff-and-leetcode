class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count=0
        con=0
        for i in range(len(operations)):
            if operations[i]=="++X" or operations[i]=="X++":
                count+=1
            else:
                con+=1
        return (count-con)
