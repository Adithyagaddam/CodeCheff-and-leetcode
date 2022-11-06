class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        r=0
        q=[]
        seats.sort()
        students.sort()
        for i in range(len(students)):
            s=abs(seats[i]-students[i])
            q.append(s)
        for i in range(len(q)):
            r=q[i]+r
        return r
