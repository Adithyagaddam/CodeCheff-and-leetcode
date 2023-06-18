# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        s=[]
        while q:
            temp=q.popleft()
            r=[]
            if temp:
                r.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)
            if r:
                s.append(r[0])
        
        t=list(set((s)))
        t.sort()
        print(t)
        if len(t)>1:
            return t[1]
        else:
            return -1
