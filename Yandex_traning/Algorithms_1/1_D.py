def main(a, b, c):
    if c < 0:
        print('NO SOLUTION')
    elif a == 0 and b == c**2:
        print('MANY SOLUTIONS')
    elif a == 0 and b != c**2:
        print('NO SOLUTION')
    else:
        x = (c**2 - b) / a
        if x != int(x):
            print('NO SOLUTION')
        else:
            print(int(x))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    main(a, b, c)

