class Solution(object):
    def countBits(self, n):
        res = list()
        while n != 0:
            res.append(bin(n)[2:].count('1'))
            n -= 1
        res.append(0)
        return res[::-1]
