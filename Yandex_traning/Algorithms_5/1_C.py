def main():
    n = int(input())
    cnt = 0

    for _ in range(n):
        x = int(input())
        if x < 3:
            cnt += x

        else:
            cnt += x//4
            x %= 4
            if x < 3:
                cnt += x

            else:
                cnt += 2
    return cnt

if __name__ == "__main__":
    print(main())