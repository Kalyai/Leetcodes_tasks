class Solution(object):
    def getSum(self, a, b):
        
        while b != 0:
            sdvig = (a & b) << 1
            a = a ^ b
            b = sdvig
        return a

res = Solution().getSum(-1, 1)
print(res)