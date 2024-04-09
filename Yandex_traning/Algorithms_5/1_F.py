def main(n, dig):
    res = ''
    now = 0

    i = 0
    while i < n:
        x = dig[i]
        if not(now):
            if (x % 2 == 0 and dig[i + 1] % 2 == 1) or (dig[i + 1] % 2 == 0 and x % 2 == 1):
                res += '+'
                now = 1
                i += 1

            elif x % 2 == 1 and dig[i + 1] % 2 == 1:
                res += 'x'
                now = 1
                i += 1

            else: res += '+'

        else:
            if x % 2 == 0:
                res += '+'
            else:
                res += 'x'
        i += 1
    return res

if __name__ == '__main__':
    n = int(input())
    dig = list(map(int, input().split()))
    print(main(n, dig))