class Solution:
    def reverseBits(self, n):
        z = '0' * (32 - len(bin(n)[2:]))
        n = z + bin(n)[2:]
        n = n[::-1]
        return int(n, 2)
