class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[i] + 1, dp[j])
                    if dp[j] > result:
                        result = dp[j]
        return result
