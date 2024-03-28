class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        result = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                result = max(prices[right] - prices[left], result)
                right += 1
        return result
