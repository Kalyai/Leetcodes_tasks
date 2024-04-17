# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        def helper(root):
            if root is None:
                return

            helper(root.left)
            result[0] -= 1
            if result[0] == 0:
                if result[1] == 0:
                    result[1] = root.val
                return
            helper(root.right)

        result = [k, 0]
        helper(root)
        return result[1]
