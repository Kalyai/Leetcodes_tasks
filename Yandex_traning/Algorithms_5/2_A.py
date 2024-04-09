def main(n):
    mi_x, mi_y = map(int, input().split())
    ma_x, ma_y = mi_x, mi_y

    for i in range(n - 1):
        x, y = map(int, input().split())
        
        if ma_x < x:
            ma_x = x
        elif mi_x > x:
            mi_x = x

        if ma_y < y:
            ma_y = y
        elif mi_y > y:
            mi_y = y

    return (mi_x, mi_y, ma_x, ma_y)

if __name__ == '__main__':
    n = int(input())
    print(main(n))