def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if max(a, b, c) < min(a, b, c) + (a + b + c - max(a, b, c) - min(a, b, c)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()