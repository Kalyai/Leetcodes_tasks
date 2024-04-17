class Solution(object):
    def evenOddBit(self, n):
        even, odd = 0, 0

        count_operation = 0
        while n > 0:
            if n % 2 == 1 and count_operation % 2 == 0:
                even += 1

            if n % 2 == 1 and count_operation % 2 == 1:
                odd += 1

            n //= 2
            count_operation += 1

        return [even, odd]