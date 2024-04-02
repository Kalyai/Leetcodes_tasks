#Дана строка S, состоящая из строчных латинских букв.
#Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.
#Пример:
#abracadabra
#2
#4 0 6 - yes
#3 1 6 - no

s = str(input())
n = int(input())
l_s = len(s)
h = [0] * (l_s + 1)
x_len = [0] * (l_s + 1)
x_len[0] = 1
x = 10
p = 10 ** 9 + 9
for i in range(1, l_s + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    x_len[i] = (x_len[i - 1] * x) % p

def comparision(from1, from2, l):
    return (
            (h[from1 + l - 1] + (h[from2 - 1] * x_len[l])) % p ==
            (h[from2 + l - 1] + (h[from1 - 1] * x_len[l])) % p
    )


for i in range(n):
    l, a, b = map(int, input().split())
    a += 1
    b += 1
    from1 = max(a, b)
    from2 = min(a, b)
    if comparision(from1, from2, l):
        print('yes')
    else:
        print('no')
