def main(a, b, n, m):
    mina = a * (n - 1) + n
    maxa = a * (n + 1) + n

    minb = b * (m - 1) + m
    maxb = b * (m + 1) + m

    min_ma = min(maxa, maxb)
    max_mi = max(mina, minb)

    if min_ma < max_mi:
        print(-1)
    else:
        print(max_mi, min_ma)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())
    main(a, b, n, m)