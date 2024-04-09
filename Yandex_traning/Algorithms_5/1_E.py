def main(n, k, d):
    fl = 0
    for i in range(0, 10):
        if (n * 10 + i) % k == 0:
            n = n * 10 + i
            fl = 1
            break

    if not(fl):
        return -1
    return str(n) + '0' * (d - 1)

if __name__ == '__main__':
    n, k, d = map(int, input().split())
    print(main(n, k, d))