# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    answer = -1000
    def maxPathSum(self, root):
        self.dfs(root)
        res = Solution.answer
        Solution.answer = -1000
        return res

    def dfs(self, node):
        if node is None:
            return 0

        max_right_node = max(self.dfs(node.right), 0)
        max_left_node = max(self.dfs(node.left), 0)
        Solution.answer = max(Solution.answer, max_right_node + max_left_node + node.val)
        return max(max_right_node, max_left_node) + node.val
