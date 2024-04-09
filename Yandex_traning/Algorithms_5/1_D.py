def R(x, y):
    i = x
    j = y
    while i > 0:
        i -= 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break
    i = x
    while i < 7:
        i += 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break
    i = x
    j = y
    while j > 0:
        j -= 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break
    j = y
    while j < 7:
        j += 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break

def B(x, y):
    i, j = x, y
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break

    i, j = x, y
    while i > 0 and j < 7:
        i -= 1
        j += 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break

    i, j = x, y
    while i < 7 and j > 0:
        i += 1
        j -= 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break

    i, j = x, y
    while i < 7 and j < 7:
        i += 1
        j += 1
        if pole[i][j] == '*':
            s = pole[i]
            s = s[:j] + '1' + s[j + 1:]
            pole[i] = s
        elif pole[i][j] in 'RB':
            break

if __name__ == '__main__':
    pole = []
    for i in range(8):
        pole.append(input())

    for i in range(8):
        for j in range(8):
            if pole[i][j] == 'R':
                R(i, j)
            elif pole[i][j] == 'B':
                B(i, j)

    cnt = 0
    for i in pole:
        cnt += i.count('*')
    print(cnt)


