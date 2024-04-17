class Solution(object):
    def isValidBST(self, root):
        def helper(root, last):
            if root is None:
                return

            helper(root.left, last)
            if last[0] and last[0].val >= root.val:
                result[0] = False
                return

            last[0] = root
            helper(root.right, last)

        last = [None]
        result = [True]
        helper(root, last)
        return result[0]