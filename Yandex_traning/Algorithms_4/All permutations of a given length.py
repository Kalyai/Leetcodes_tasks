#По данному числу N (0 < N < 10) выведите все перестановки чисел от 1 до N в лексикографическом порядке.
from itertools import permutations
n = int(input())
arr = [str(i) for i in range(1, n + 1)]


for i in permutations(arr):
    s = ''.join(i)
    print(s)
