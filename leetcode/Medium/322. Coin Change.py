class Solution(object):
    def coinChange(self, coins, amount):
            dp = [amount + 1] * (amount + 1)
            dp[0] = 0

            for i in range(1, len(dp)):
                for c in coins:
                    if i >= c:
                        dp[i] = min(dp[i], 1 + dp[i - c])

            return dp[amount] if dp[amount] != amount + 1 else -1
