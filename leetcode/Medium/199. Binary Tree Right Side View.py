# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        def view_nodes(left, right, height):
            if right:
                if height + 1 > len(result):
                    result.append(right.val)
                    view_nodes(right.left, right.right, height + 1)
                else:
                    view_nodes(right.left, right.right, height + 1)
            if left:
                if height + 1 > len(result):
                    result.append(left.val)
                    view_nodes(left.left, left.right, height + 1)
                else:
                    view_nodes(left.left, left.right, height + 1)

        if root is None:
            return []

        result = [root.val]
        view_nodes(root.left, root.right, 1)
        return result

