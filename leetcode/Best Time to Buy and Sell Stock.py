class Solution(object):
    def maxProfit(self, prices):
        mi, ma = 10**5+1, 0
        for i in range(len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            if prices[i] - mi > ma:
                ma = prices[i] - mi
        return ma
res = Solution().maxProfit([7,4,1,2])
print(res)
