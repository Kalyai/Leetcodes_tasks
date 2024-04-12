# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        def helper(root):
            if root is None:
                return
            
            left_max = max(helper(root.left), 0)
            right_max = max(helper(root.right), 0)
            result[0] = max(result[0], left_max + right_max + root.val)

            return max(left_max, right_max) + root.val

        result = [-1000]
        helper(root)
        return result[0]
