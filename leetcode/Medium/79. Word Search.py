class Solution(object):
    def exist(self, board, word):
        def dfs(r, c, l):
            if l == len(word):
                return True

            if c < 0 or r < 0 \
                or c >= len(board[0]) or r >= len(board) \
                or word[l] != board[r][c] or \
                (r, c) in path:
                return False

            path.add((r, c))
            res = (dfs(r, c + 1, l + 1) or
                   dfs(r, c - 1, l + 1) or
                   dfs(r + 1, c, l + 1) or
                   dfs(r - 1, c, l + 1))
            path.remove((r, c))
            return res


        path = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
res = Solution().exist(board, word)
print(res)
