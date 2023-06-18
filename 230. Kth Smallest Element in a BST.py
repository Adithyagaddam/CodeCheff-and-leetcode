# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
        s.sort()
        return s[k-1]
