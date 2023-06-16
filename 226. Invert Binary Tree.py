# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        s=[]
        q.append(root)
        r=[]
        while q:
            k=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp:
                    k.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if k:
                for i in range(len(k)):
                    r.append(k[i])
        return r
