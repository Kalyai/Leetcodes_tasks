def main(p, v, q, m):
    if p > q:
        if p - v <= q + m:
            mi = min(p - v, q - m)
            ma = max(p + v, q + m)
            return (ma - mi + 1)
        return (2*m + 1) + (2*v + 1)

    if p + v >= q - m:
        mi = min(p - v, q - m)
        ma = max(p + v, q + m)
        return (ma - mi + 1)
    return (2*m + 1) + (2*v + 1)

if __name__ == '__main__':
    p, v = map(int, input().split())
    q, m = map(int, input().split())
    print(main(p, v, q, m))