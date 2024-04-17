# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height < 0 or right_height < 0 or abs(right_height - left_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return height(root) >= 0