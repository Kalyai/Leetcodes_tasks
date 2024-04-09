def main(number, n1, n2, n3):
    def check_number(n):
        n_cache = str()
        for i in n:
            if 48 <= ord(i) <= 57:
                n_cache+=i
        if n[0] == '+' and n[1] == '7':
            n_cache = '8' + n_cache[1:]
        if len(n_cache) == 7:
            n_cache = '8495' + n_cache

        return n_cache

    def check_cache(n1, n2):
        if n1 == n2:
            return 'YES'
        return 'NO'

    n1_cache = check_number(n1)
    n2_cache = check_number(n2)
    n3_cache = check_number(n3)
    number_cache = check_number(number)

    print(check_cache(number_cache, n1_cache))
    print(check_cache(number_cache, n2_cache))
    print(check_cache(number_cache, n3_cache))

if __name__ == '__main__':
    number = input()
    n1 = input()
    n2 = input()
    n3 = input()
    main(number, n1, n2, n3)