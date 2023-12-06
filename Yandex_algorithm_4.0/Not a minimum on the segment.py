#На каждый запрос выведите в отдельной строке ответ — любой элемент на [L, R], кроме минимального. 
#В случае, если такого элемента нет, выведите "NOT FOUND".
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
	fl = 1
	l, r = map(int, input().split())
	while r > l:
		if arr[r] > arr[l]:
			print(arr[r])
			fl = 0
			break
		elif arr[l] > arr[r]:
			fl = 0
			print(arr[l])
			break
		else:
			r -= 1
	if fl:
		print('NOT FOUND')
