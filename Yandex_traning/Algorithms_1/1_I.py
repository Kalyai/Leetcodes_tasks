def main(a, b, c, d, e):
    def sort2(a, b):
        if a < b: return a, b
        return b, a

    d, e = sort2(d, e)
    a, b = sort2(a, b)
    b, c = sort2(b, c)
    a, b = sort2(a, b)
    if a <= d and b <= e:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(main(a, b, c, d, e))
