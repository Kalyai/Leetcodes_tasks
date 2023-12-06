a, b, c, d = map(int, input().split())
if b != d:
    n = b * d
    m = a * d + c * b
else:
    n = b
    m = a + c
n1 = n
m1 = m
while m != 0 and n != 0:
    if m > n:
        m -= n
    else:
        n -= m
NOD = max(n, m)
m1 //= NOD
n1 //= NOD
print(m1, n1)
