k = int(input())
n = int(input())
pupils = list()
for i in range(n):
    pupil = int(input())
    pupils.append(pupil)

pupils = [0] + pupils
cnt = 0
lift = 0
i = 0

while i < n + 1:
    pupil = pupils[i]
    if pupil >= k:
        pupils[i] = pupil % k
        pupil //= k
        cnt += i*pupil*2
    i += 1


i = -1

while abs(i) <= n:
    pupil = pupils[i]
    if lift == 0:
        if pupil == 0:
            while abs(i) <= n and pupil == 0:
                i -= 1
                pupil = pupils[i]
        cnt += (n + i + 1)
        lift = pupil
        pupil = 0
        pupils[i] = 0

    if lift != 0:
        while pupil + lift < k and abs(i) <= n:
            if pupil != 0:
                lift += pupil
            i -= 1
            cnt += 1
            pupil = pupils[i]

        if pupil + lift == k:
            cnt += (n + i + 1)
            lift = 0
            pupil = 0
            pupils[i] = 0

        else:
            lift = pupil + lift - k
            cnt += (n + i + 1) * 2
            pupils[i] = 0
            pupil = 0


print(cnt)
