#Выведите n чисел через пробел, i-е из которых будет обозначать 
#уровень недовольства группы при выборе i-го студента старостой.
n = int(input())
students = list(map(int, input().split()))

pr = [0] * (n + 1)
for i in range(1, n + 1):
    pr[i] = pr[i - 1] + students[i - 1]

sm = sum(students)
res = list()
for i in range(n):
    sm = abs(sm - students[i])
    result = sm - (students[i] * (n - i - 1))
    student = students[i]
    result += abs((pr[i] - students[i] * i))
    res.append(result)

print(*res)
