# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        if ((p is None) and q) or (p and (q is None)):
            return False
        elif p and q and (p.val != q.val):

            
            return False
            
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return True
        
