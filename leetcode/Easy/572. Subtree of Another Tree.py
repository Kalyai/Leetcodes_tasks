# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def search(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False

            return subRoot.val == root.val and search(root.left, subRoot.left) and search(root.right, subRoot.right)

        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False

        return search(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
