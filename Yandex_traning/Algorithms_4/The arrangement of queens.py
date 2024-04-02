#Расставить н ферзей на поле н*н, чтобы они не атакавали друг друга
n = int(input())
board = [[0 for i in range(n)] for j in range(n)]
def Queen(i, j, n):
    for x in range(n):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i - j + x < n:
            board[i - j + x][x] += 1
        if 0 <= i + j - x < n:
            board[i + j - x][x] += 1
    board[i][j] = -1


def del_Queen(i, j, n):
    for x in range(n):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i - j + x < n:
            board[i - j + x][x] -= 1
        if 0 <= i + j - x < n:
            board[i + j - x][x] -= 1
    board[i][j] = 0


def printPosition(n):
    win = list()
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                win.append('1')

cnt = 0
def solve(i, n):
    for j in range(n):
        if board[i][j] == 0:
            Queen(i, j, n)
            if i != n - 1:
                solve(i + 1, n)
            else:
                global cnt
                cnt += 1
            del_Queen(i, j, n)

solve(0, n)
print(cnt)
