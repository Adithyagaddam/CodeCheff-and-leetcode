class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        while l1:
            list1.append(str(l1.val))
            l1=l1.next
        while l2:
            list2.append(str(l2.val))
            l2=l2.next
        k=int(''.join(list1))
        s=int(''.join(list2))
        p=(k+s)
        res = [int(x) for x in str(p)]
        q=ListNode(0)
        r=q
        for i in res:
            r.next=ListNode(i)
            r=r.next
        return q.next
