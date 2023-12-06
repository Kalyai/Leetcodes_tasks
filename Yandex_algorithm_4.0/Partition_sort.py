n = int(input())
arr = list(map(int, input().split()))
x = int(input())

cnt_l = 0
cnt_r = 0
for i in range(n):
    if arr[i] < x:
        cnt_l += 1
    else:
        cnt_r += 1
print(cnt_l)
print(cnt_r)
