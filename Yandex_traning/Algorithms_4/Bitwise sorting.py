n = int(input())
arr = list()
ma_len_digit = -1
for i in range(n):
    x = str(input())
    ma_len_digit = max(ma_len_digit, len(x))
    arr.append(x)
print('Initial array:')
pr = ''
for x in arr:
    pr = pr + x + ', '
pr = pr[:-2]
print(pr)
print('**********')
buckets = [[] for i in range(10)]
print('Phase 1')
for x in arr:
    buckets[int(x[-1])].append(x)
for i in range(10):
    if buckets[i] == []:
        print('Bucket ' + str(i) +': empty')
    else:
        pr = ''
        for x in buckets[i]:
            pr = pr + x + ', '
        pr = pr[:-2]
        print('Bucket ' + str(i) + ': ' + pr)
for j in range(1, ma_len_digit):
    print('**********')
    print('Phase ' + str(j+1))
    new_buckets = [[] for i in range(10)]
    for x in range(10):
        if buckets[x] == []:
            continue
        else:
            for x1 in buckets[x]:
                new_buckets[int(x1[-j-1])].append(x1)
    buckets = new_buckets.copy()
    for i in range(10):
        if buckets[i] == []:
            print('Bucket ' + str(i) +': empty')
        else:
            pr = ''
            for x in buckets[i]:
                pr = pr + x + ', '
            pr = pr[:-2]
            print('Bucket ' + str(i) + ': ' + pr)
print('**********')
res = list()
for i in range(10):
    res.extend(buckets[i])
print('Sorted array:')
pr = ''
for x in res:
    pr = pr + x + ', '
pr = pr[:-2]
print(pr)
