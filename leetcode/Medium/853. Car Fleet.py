class Solution(object):
    def carFleet(self, target, position, speed):
        n = len(position)

        cars = dict()
        for i in range(n):
            if position[i] not in cars:
                cars[position[i]] = 0
            cars[position[i]] = max(cars[position[i]], round((float(target - position[i]) / speed[i]) * 10**6))

        min_position = sorted(position)
        cnt = n
        stack = []
        for i in range(n):
            while stack and cars[min_position[i]] >= stack[-1]:
                stack.pop()
                cnt -= 1
            stack.append(cars[min_position[i]])
        return cnt
