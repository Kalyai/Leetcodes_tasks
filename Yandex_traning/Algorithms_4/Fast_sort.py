import sys

n = int(input())
arr = list(map(int, input().split()))

sys.setrecursionlimit(10000)
def quick_sort(n, arr):
    if n < 2:
        return arr

    equal, greater = 0, 1
    arr[0], arr[n//4] = arr[n//4], arr[0]
    for i in range(1, n):
        if arr[i] == arr[equal]:
            arr[i], arr[greater] = arr[greater], arr[i]
            greater += 1
        elif arr[i] < arr[equal]:
            arr[i], arr[greater], arr[equal] = arr[greater], arr[equal], arr[i]
            equal += 1
            greater += 1

    return quick_sort(equal, arr[:equal]) + arr[equal:greater] + quick_sort(n - greater, arr[greater:])

print(*quick_sort(n, arr))
