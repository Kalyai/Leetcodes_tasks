class Solution(object):
    def isValidSudoku(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digital = board[i][j]
                    for c in range(9):
                        c_i = i
                        c_j = c
                        if (i != c_i or j != c_j) and board[c_i][c_j] == digital:
                            return False

                    for c in range(9):
                        c_i = c
                        c_j = j
                        if (i != c_i or j != c_j) and board[c_i][c_j] == digital:
                            return False

                    ki = i // 3
                    kj = j // 3
                    for i3 in range(3 * ki, 3 * (ki + 1)):
                        for j3 in range(3 * kj, 3 * (kj + 1)):
                            if (i != i3 or j != j3) and board[i3][j3] == digital:
                                return False

        return True
