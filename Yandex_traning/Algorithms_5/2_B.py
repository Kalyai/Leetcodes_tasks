def main(n, k, fish):
    res = 0
    for i in range(n):
        mi = fish[i]
        ma = 1

        for j in range(i + 1, min(k + i + 1, n)):
            ma = max(fish[j], ma)
        res = max(ma - mi, res)

    return res

if __name__ == '__main__':
    n, k = map(int, input().split())
    fish = list(map(int, input().split()))
    print(main(n, k, fish))