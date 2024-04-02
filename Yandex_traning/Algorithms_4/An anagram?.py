str1 = str(input())
str2 = str(input())
hash = dict()
for i in str1:
    hash[i] = 0
for i in str2:
    if i in hash:
        hash[i] += 1
cnt = 0
fl = 1
for i in hash:
    if hash[i] > 0:
        cnt += hash[i]
    else:
        fl = 0
        print('NO')
        break
if cnt == len(str1) == len(str2):
    print('YES')
elif fl:
    print('NO')
