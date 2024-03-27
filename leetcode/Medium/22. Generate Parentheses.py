class Solution(object):
    def generateParenthesis(self, n):
        def make(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                make(s + '(', left + 1, right)
            if right < left:
                make(s + ')', left, right + 1)

        result = []
        make()
        return result
