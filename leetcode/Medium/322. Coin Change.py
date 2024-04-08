class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(1 + dp[i - coin], dp[i])

        return dp[-1] if dp[-1] != amount + 1 else -1
