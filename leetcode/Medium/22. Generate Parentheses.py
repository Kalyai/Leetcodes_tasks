class Solution(object):
    def generateParenthesis(self, n):
        parentheses = list()

        def main(string, n, left, right):
            if len(string) == 2 * n:
                parentheses.append(string)
                return

            if left < n:
                main(string + '(', n, left + 1, right)
            if left > right:
                main(string + ')', n, left, right + 1)

        main('', n, 0, 0)
        return parentheses
