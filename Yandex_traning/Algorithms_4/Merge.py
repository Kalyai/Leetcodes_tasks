n = int(input())
arr_f = list(map(int, input().split()))
m = int(input())
arr_s = list(map(int, input().split()))
res = list()

f = 0
s = 0
while f < n and s < m:
    if arr_f[f] < arr_s[s]:
        res.append(arr_f[f])
        f += 1
    elif arr_f[f] == arr_s[s]:
        res.append(arr_f[f])
        res.append(arr_s[s])
        f += 1
        s += 1
    else:
        res.append(arr_s[s])
        s += 1
if f != n:
    if res != []:
        res += arr_f[f:]
    else:
        res = arr_f[f:].copy()
if s != m:
    if res != []:
        res += arr_s[s:]
    else:
        res = arr_s[s:].copy()
if res == []:
    print(0)
else:
    print(*res)
