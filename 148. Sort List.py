# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l.sort()
        t=ListNode(0)
        a=t
        for i in l:
            a.next=ListNode(i)
            a=a.next
        return t.next
